import os
import logging
from source.dirtositemap import DirToSitemap
from source.config import *
from source.sitemaptree import SitemapTree


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
    sitemap = DirToSitemap(dir=new_dir, html=HTMLSUFFIX, root_url=ROOTURL, home_page=HOMEPAGE,
                           change_freq=CHANGEFREQ_PATTERNS[3], nsmap=XMLNS)
    sitemap.add_homepage()
    pt = sitemap.parse_dir("")

    pt_old = SitemapTree(file=old_sitemap)
    path_file_dic = parse_dir(old_dir)
    for rpath, file in path_file_dic.items():
        old_apath, new_apath = os.path.join(old_dir, rpath), os.path.join(new_dir, rpath)
        if os.path.exists(new_apath) and os.path.exists(old_apath):
            if cmp_file(old_apath, new_apath) is True:  # 更新lastmod
                if sitemap.html is True:
                    url_html = sitemap.path_to_url(rpath)
                    new_node = pt.get_node(url_html)
                else:
                    url_html = sitemap.path_to_url(rpath)+'.html'
                    new_node = pt.get_node(url_html[0:-5])

                old_node = pt_old.get_node(url_html)
                if old_node is None:# 可能旧的sitemap中url不是以xml结尾
                    old_node = pt_old.get_node(url_html[0:-5])
                if old_node is None:# 没有找到对应的sitemap结点
                    logging.error("no site map for file in {}".format(old_apath))
                    continue
                logging.info("change file {} lastmod".format(rpath))
                old_lastmod = old_node.find('lastmod', namespaces=old_node.nsmap).text
                new_node.find('lastmod', namespaces=new_node.nsmap).text = old_lastmod
    return pt


if __name__ == "__main__":
    html = r"D:\研一\sitemap\sitemap_generator\example\test"
    html_old = r'D:\研一\sitemap\sitemap_generator\example\test_old'
    old_sitemap = r"D:\研一\sitemap\sitemap_generator\example\test_old.xml"
    pt = compare(html_old,html,old_sitemap)
    pt.save(r"D:\研一\sitemap\sitemap_generator\example\test.xml")
