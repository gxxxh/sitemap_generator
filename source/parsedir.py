import os,logging
import source.config as config
from source.sitemaptree import SitemapTree
from datetime import date

class ParseDir:
    def __init__(self,dir_name):
        """
        init a sitemap tree
        :param xmlns:
        """
        self.sitemap_tree = SitemapTree(config.xmlns)
        self.root_path = os.path.join(config.work_path,dir_name)
        self.add_dir(self.root_path)

    @staticmethod
    def path_to_url(path):
        url = path
        return url

    @staticmethod
    def url_to_path(url):
        pass

    def add_file(self,path):
        paras = {}
        paras['loc'] = self.path_to_url(path)
        paras['lastmod']= date.strftime('%Y-%m-%dT%H:%M:%S+00:00')
        paras['changefreq'] = config.change_freq
        paras['priority']= config.priority
        cur_node = self.sitemap_tree.add_url(paras)


    # 错了，不是构建文件树
    def add_dir(self,path):
        for file in  os.listdir(path):
            temp_path = os.path.join(path,file)
            if os.path.isfile(temp_path):
                self.add_file(temp_path)
            else:
                self.add_dir(temp_path)