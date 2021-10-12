import logging
from lxml import etree
import email.utils as eut


class Sitemap:
    urlset = None
    encoding = 'UTF-8'
    xmlns = 'http://www.sitemaps.org/schemas/sitemap/0.9'

    def __init__(self):
        self.root()
        self.children()
        self.xml()

    def done(self):
        logging.info("Done")

    def root(self):
        self.urlset = etree.Element('urlset')
        self.urlset.attrib['xmlns'] = self.xmlns

    def children(self,checked):
        for index, obj in enumerate(checked):
            url = etree.Element('url')
            loc = etree.Element('loc')
            lastmod = etree.Element('lastmod')
            changefreq = etree.Element('changefreq')
            priority = etree.Element('priority')

            loc.text = obj['url']
            lastmod_info =  None
            lastmod_header = None
            lastmod.text = None

            if hasattr(obj['obj'], 'info'):
                lastmod_info = obj['obj'].info()
                lastmod_header = lastmod_info.getheader('Last-Modified')

            # check if 'Last-Modified' header exists
            if lastmod_header != None:
                lastmod.text = FormatDate(lastmod_header)

            if loc.text != None:
                url.append(loc)

            if lastmod.text != None:
                url.append(lastmod)

            if changefreq.text != None:
                url.append(changefreq)

            if priority.text != None:
                url.append(priority)

            self.urlset.append(url)

    def xml(self,filename):
        try:
            f = open(filename, 'w')
        except IOError as err:
            logging.error('file open error'+str(err))
            
        print >> f, etree.tostring(self.urlset, xml_declaration = True, encoding = self.encoding)
        f.close()

        logging.info('sitemap saved in: ',filename)

def FormatDate(datetime):
    datearr = eut.parsedate(datetime)
    date = None

    try:
        year = str(datearr[0])
        month = str(datearr[1])
        day = str(datearr[2])

        if int(month) < 10:
            month = '0' + month

        if int(day) < 10:
            day = '0' + day

        date = year + '-' + month + '-' + day
    except IndexError:
        print(datearr)

    return date