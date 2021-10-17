import os
import logging
from dirtositemap import DirToSitemap
from config import *
from sitemaptree import SitemapTree


def cmp_file(f1, f2):
    st1 = os.stat(f1)
    st2 = os.stat(f2)

    # 比较文件大小
    if st1.st_size != st2.st_size:
        return False

    bufsize = 8 * 1024
    with open(f1, 'rb') as fp1, open(f2, 'rb') as fp2:
        while True:
            b1 = fp1.read(bufsize)  # 读取指定大小的数据进行比较
            b2 = fp2.read(bufsize)
            if b1 != b2:
                return False
            if not b1:
                logging.info("{} and {} isn't change".format(f1, f2))
                return True


def parse_dir(dir, cur_path=""):
    """
    获取文件夹中html文件以及其路径
    :param dir: 目录名称（绝对路径）
    :return: dict{rpath:filename}
    """
    result = {}
    apath = os.path.join(dir, cur_path)
    files = os.listdir(apath)
    for file_name in files:
        temp_path = os.path.join(apath, file_name)
        rpath = os.path.join(cur_path, file_name)
        if os.path.isfile(temp_path):
            if file_name[-5:] == '.html':
                result[rpath] = file_name
        else:
            result.update(parse_dir(dir, rpath))
    return result


def compare(old_dir, new_dir, old_sitemap, ):
    """

    :param old_dir: 绝对路径
    :param new_dir: 绝对路径
    :param old_sitemap: html_old对应的sitemap
    :return:
    """
    # sitemaptree for dir html
    sitemap = DirToSitemap(dir=new_dir, html=HTMLSUFFIX, root_url=ROOTURL, home_page=HOMEPAGE,
                           change_freq=CHANGEFREQ_PATTERNS[3], nsmap=XMLNS, priorities=PRIORITIES, time_zone=TIMEZONE,
                           time_pattern=LASTMODFORMAT)
    # sitemap.add_homepage()
    pt = sitemap.parse_dir("")

    # sitemaptree for dir html_old
    pt_old = SitemapTree(file=old_sitemap)
    path_file_dic = parse_dir(old_dir)
    for rpath, file in path_file_dic.items():
        old_apath, new_apath = os.path.join(old_dir, rpath), os.path.join(new_dir, rpath)
        if os.path.exists(new_apath) and os.path.exists(old_apath):
            if cmp_file(old_apath, new_apath) == True:  # 更新lastmod
                url_html = sitemap.path_to_url(rpath, True)
                url_nhtml = sitemap.path_to_url(rpath, False)
                if sitemap.html == True:
                    new_node = pt.get_node(url_html)
                else:
                    new_node = pt.get_node(url_nhtml)

                if new_node == None:
                    logging.error(
                        "the node in new sitemap should not be none, path is {},url is {}".format(rpath, url_html))
                old_node = pt_old.get_node(url_html)
                if old_node == None:  # 可能旧的sitemap中url不是html结尾
                    old_node = pt_old.get_node(url_nhtml)

                if old_node == None:  # 没有找到对应的sitemap结点
                    logging.error("no site map for file in {}".format(old_apath))
                    continue
                logging.info("change file {} lastmod".format(rpath))
                old_lastmod = old_node.find('lastmod', namespaces=old_node.nsmap).text
                sitemap.change_lastmod(new_node, old_lastmod, sitemap.tp)
    return pt


if __name__ == "__main__":
    logging.basicConfig(level=logging.ERROR,  # 控制台打印的日志级别
                        format=LOGGINTFORMAT,
                        )
    # 对比html和html_old生成sitemap
    # html = HTMLPATH
    # html_old = HTMLOLDPATH
    # old_sitemap = OLDSITEMAPPATH
    # pt = compare(html_old, html, old_sitemap)
    # pt.sort()
    # pt.save(NEWSITEMAPPATH)

    # 通过文件夹直接生成sitemap
    dir_path = HTMLPATH
    sitemap = DirToSitemap(dir=dir_path, html=HTMLSUFFIX, root_url=ROOTURL, home_page=HOMEPAGE,
                           change_freq=CHANGEFREQ_PATTERNS[3], nsmap=XMLNS, priorities=PRIORITIES, time_zone=TIMEZONE,
                           time_pattern=LASTMODFORMAT)
    # sitemap.add_homepage()
    pt = sitemap.parse_dir("")
    pt.sort()
    pt.save(NEWSITEMAPPATH)
