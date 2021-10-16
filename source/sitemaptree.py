import logging
import source.config as config
from lxml import etree


class SitemapTree:
    def __init__(self, namespace=config.XMLNS, file=""):
        """
        urlset is a list of URLs that should appear in the sitemap
        :param namespace: html namespace
        :param file: xml文件，若为空则创建空的url set, 否则直接从文件中解析
        """
        if file == "":  # 初始化一个只有根节点的sitemaptree
            self.etree=None
            self.urlset = etree.Element('urlset')
            self.nsmap = namespace
            self.urlset.attrib['xmlns'] = self.nsmap
        else:  # 从xml文件中读取sitemaptree
            self.etree = etree.parse(file, etree.XMLParser())
            self.urlset = self.etree.getroot()
            self.nsmap = self.urlset.nsmap

    def get_root(self):
        """
        get etree root node
        :return:
        """
        return self.urlset

    @staticmethod
    def get_lastmod(url_node):
        cnodes = url_node.getnodes()


    def get_node(self, url):
        """
        find node by its url
        :param url: url of the html
        :return: url node
        """
        cnodes = self.urlset.getchildren()
        for cnode in cnodes:
            loc_node = cnode.find('loc', namespaces=cnode.nsmap)
            if loc_node is None:
                logging.error("there should be a loc in url")
            if url == loc_node.text:
                return cnode
        return None

    def add_url(self, **kwargs):
        """
        add a url to urlset
        :param loc: url
        :param lastmod: time
        :param changefreq: change frequency
        :param priority:
        :return: etree node
        """
        url = etree.Element('url')
        # loc
        loc = etree.Element('loc')
        if kwargs.get('loc') != None:
            loc.text = kwargs['loc']
        else:
            logging.error('the url is None')
            return None
        url.append(loc)

        lastmod = etree.Element('lastmod')
        if kwargs.get('lastmod') != None:
            # lastmod.text = date.strftime('%Y-%m-%dT%H:%M:%S+00:00')
            lastmod.text = kwargs['lastmod']
        else:
            logging.error(url + 'does not have last modified time')
            return None
        url.append(lastmod)

        changefreq = etree.Element('changefreq')
        if kwargs.get('changefreq') != None:
            changefreq.text = kwargs['changefreq']
        else:
            changefreq.text = 'weekly'
        url.append(changefreq)

        priority = etree.Element('priority')
        if kwargs.get('priority') != None:
            priority.text = str(kwargs['priority'])
        else:
            priority.text = str(0.5)
        url.append(priority)

        self.urlset.append(url)
        return url

    def save(self, file_name):
        """
        savt sitemap to xml
        :param file_name:
        :return:
        """
        try:
            f = open(file_name, 'wb')
            f.write(etree.tostring(self.urlset, xml_declaration=True, encoding=config.ENC_UTF8))
            f.close()
            logging.info('Sitemap saved in: ', file_name)
        except:
            logging.error("save " + file_name + " sitemap failed")
