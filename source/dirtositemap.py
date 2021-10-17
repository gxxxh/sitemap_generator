import os, platform, logging
from sitemaptree import SitemapTree
from datetime import datetime, timezone, timedelta


class DirToSitemap:
    def __init__(self, dir, html, root_url, home_page, change_freq, nsmap, priorities, time_zone, time_pattern):
        """
        初始化一个sitemap对象
        :param dir: 文件夹目录
        :param html: sitemap中是否包含".html"后缀
        :param root_url: 根域名
        :param home_page: 主页文件名
        :param change_freq: 网页修改频率
        :param nsmap: sitemap格式
        """
        self.sitemap_tree = SitemapTree(namespace=nsmap, file="")
        self.dir_path = dir
        self.html = html
        self.root_url = root_url
        self.home_page = home_page
        self.change_freq = change_freq
        self.priorities = priorities
        self.tz = timezone(timedelta(hours=time_zone))
        self.tp = time_pattern
        # self.add_dir(self.dir_path)

    # def add_homepage(self):
    #     """
    #     添加主页对应的结点
    #     :return:
    #     """
    #     file_path = os.path.join(self.dir_path, self.home_page)
    #     if os.path.exists(file_path):
    #         self.add_file("", homepage=1)
    #     else:
    #         logging.error("no index.html file in the folder")

    def change_lastmod(self, node, t, timepattern):
        if t.find('+') != -1:  # %Y-%m-%dT%H:%M:%S+00:00
            if self.tp == '%Y-%m-%dT%H:%M:%S+00:00':
                node.find('lastmod', namespaces=node.nsmap).text = t
            elif self.tp == '%Y-%m-%d':
                node.find('lastmod', namespaces=node.nsmap).text = t[0:t.find('T')]
            else:
                logging.error('sitemap time pattern should be %Y-%m-%dT%H:%M:%S+00:00 or %Y-%m-%d')
        else:
            # 缺少信息，不知道时区无法补充时间信息，只能直接拷贝
            node.find('lastmod', namespaces=node.nsmap).text = t

    def path_to_url(self, rpath, html):
        """
        根据相对路径获取其对应的url
        :param rpath: 相对项目的相对路径
        :return:
        """
        # 根域名
        if rpath == self.home_page:
            return self.root_url
        if (platform.system() == 'Windows'):
            rpath = '/'.join(rpath.split('\\'))
        # 是否添加 html 后缀
        if html is True:
            if rpath[-5:] != ".html":
                rpath = rpath + ".html"
        else:
            if rpath[-5:] == ".html":
                rpath = rpath[0:-5]
        url = self.root_url + '/' + rpath
        return url

    @staticmethod
    def url_to_path(url):
        pass

    def get_priority(self, rpath):
        """
        根据相对路径的深度获取优先级
        :param path: 相对根目录的相对路径
        :return:
        """
        if rpath == self.home_page:
            return self.priorities[0]
        if (platform.system() == 'Windows'):
            rpath = '/'.join(rpath.split('\\'))
        depth = rpath.count('/')
        return self.priorities[depth + 1]

    def add_file(self, rpath, homepage=0):
        """
        添加文件对应结点
        :param rpath: 相对路径
        :param homepage: 是否为主页
        :return:
        """
        # if homepage:
        #     url = self.root_url
        #     priority = self.priorities[0]
        # else:
        url = self.path_to_url(rpath, self.html)
        priority = self.get_priority(rpath)
        # 获得带时区的UTC时间
        current_time_utc = datetime.utcnow().replace(tzinfo=self.tz)
        lastmod = datetime.strftime(current_time_utc, self.tp)
        cur_node = self.sitemap_tree.add_url(loc=url, lastmod=lastmod, changefreq=self.change_freq, priority=priority)
        if cur_node == None:
            logging.error("add file " + rpath + " failed.")

    def parse_dir(self, rpath=""):
        """
        解析文件夹添加结点
        :param rpath: 相对项目的相对路径,默认为"",即从
        :return:
        """
        # 文件夹的绝对路径
        apath = os.path.join(self.dir_path, rpath)
        files = os.listdir(apath)
        # if (rpath == "" and self.home_page in files):
        #     files.remove(self.home_page)
        for file_name in files:
            temp_path = os.path.join(apath, file_name)
            if os.path.isfile(temp_path):
                if file_name[-5:] == '.html':
                    self.add_file(os.path.join(rpath, file_name))
            else:
                self.parse_dir(os.path.join(rpath, file_name))
        return self.sitemap_tree

    def save(self, file_name):
        """
        保存sitemap
        :param file_name: 文件路径+文件名
        :return:
        """
        self.sitemap_tree.save(file_name)
