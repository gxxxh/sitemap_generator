import os,platform, logging
import source.config as config
from source.sitemaptree import SitemapTree
from datetime import datetime, timezone, timedelta


class ParseGitPage:
    def __init__(self,dir, html,root_url):
        """
        init a sitemap tree
        """
        self.sitemap_tree = SitemapTree(config.XMLNS)
        self.dir_path = dir
        self.html = html
        self.root_url = root_url
        # self.add_dir(self.dir_path)

    def add_homepage(self):
        """
        add homepage node
        :return:
        """
        # file_path = config.work_path + '/' + config.homepage_file
        file_path = os.path.join(self.dir_path, config.HOMEPAGE)
        if os.path.exists(file_path):
            self.add_file("", homepage=1)
        else:
            logging.error("no index.html file in the folder")


    def path_to_url(self, path):
        if (platform.system() == 'Windows'):
            path = '/'.join(path.split('\\'))
        # 是否添加 html 后缀
        if self.html is True:
            if path[-5:] != ".html":
                path = path + ".html"
        else:
            if path[-5:] == ".html":
                path = path[0:-5]
        url = self.root_url + '/' + path
        return url

    @staticmethod
    def url_to_path(url):
        pass

    def add_file(self, path, homepage=0):
        """
        添加文件对应结点
        :param path: 相对路径
        :param homepage: 是否为主页
        :return:
        """
        if homepage:
            url = self.root_url
        else:
            url = self.path_to_url(path)
        tz_utc = timezone(timedelta(hours=0))
        # 获得带时区的UTC时间
        current_time_utc = datetime.utcnow().replace(tzinfo=tz_utc)
        lastmod = datetime.strftime(current_time_utc,'%Y-%m-%dT%H:%M:%S+00:00')
        # changefreq = config.change_freq
        # priority = config.priority
        cur_node = self.sitemap_tree.add_url(loc=url, lastmod=lastmod, changefreq=config.CHANGEFREQ, priority=config.PRIORITY)
        if cur_node == None:
            logging.error("add file " + path + " failed.")

    def parse_dir(self, cur_path):
        """
        解析文件夹添加结点
        :param dir_name:文件夹名称
        :param cur_path: 相对homepage的路径
        :return:
        """
        # 文件夹的绝对路径
        path = os.path.join(self.dir_path, cur_path)
        files = os.listdir(path)
        if(cur_path=="" and config.HOMEPAGE in files):
            files.remove(config.HOMEPAGE)
        for file_name in files:
            temp_path = os.path.join(path, file_name)
            if os.path.isfile(temp_path):
                if file_name[-5:]=='.html':
                    self.add_file(os.path.join(cur_path, file_name))
            else:
                self.parse_dir( os.path.join(cur_path, file_name))
        return self.sitemap_tree

    def save(self, file_name):
        self.sitemap_tree.save(file_name)
