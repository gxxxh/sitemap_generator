import os
from source.dirtositemap import DirToSitemap
from source.config import *
# html字符串





if __name__ == "__main__":
    dir = r'D:\研一\sitemap\sitemap_generator\example\test_old'
    sitemap = DirToSitemap(dir=dir, html=HTMLSUFFIX, root_url=ROOTURL, home_page=HOMEPAGE, change_freq=CHANGEFREQ_PATTERNS[3],
                           nsmap=XMLNS)
    sitemap.add_homepage()
    pt = sitemap.parse_dir("")
    sitemap.save(r"D:\研一\sitemap\sitemap_generator\example\test_old.xml")