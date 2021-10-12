import logging
from lxml import etree

class SitemapTree:
    def __init__(self, xmlns='http://www.sitemaps.org/schemas/sitemap/0.9'):
        """
        urlset is a list of URLs that should appear in the sitemap
        :param xmlns: html namespace
        """
        # self.urlset = None
        self.urlset = etree.Element('urlset')
        self.urlset.attrib['xmlns'] = xmlns

    def get_root(self):
        """
        get etree root node
        :return:
        """
        return self.urlset

    def get_node(self, url):
        """
        find node by its url
        :param url:
        :return:
        """

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
        if kwargs.get('url')!=None:
            loc.text = kwargs['url']
        else:
            logging.error('the url is None')
            return None
        url.append(loc)

        lastmod = etree.Element('lastmod')
        if kwargs.get('lastmod')!=None:
            # lastmod.text = date.strftime('%Y-%m-%dT%H:%M:%S+00:00')
            lastmod.text = kwargs['lastmod']
        else:
            logging.error(url + 'does not have last modified time')
            return None
        url.append(lastmod)

        changefreq = etree.Element('changefreq')
        if kwargs.get('changefreq')!=None:
            changefreq.text = kwargs['changefreq']
        else:
            changefreq.text = 'weekly'
        url.append(changefreq)

        priority = etree.Element('priority')
        if kwargs.get('priority')!=None:
            priority.text = kwargs['priority']
        else:
            priority.text = 0.5
        url.append(priority)

        self.urlset.append(url)
        return url

    def save(self):
        pass




