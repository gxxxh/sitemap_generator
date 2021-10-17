# dir html path
HTMLPATH = r'/mnt/d/研一/sitemap/example/html'

# dir html_old path
HTMLOLDPATH = r'/mnt/d/研一/sitemap/example/html_old'

# old sitemap path
OLDSITEMAPPATH = r"/mnt/d/研一/sitemap/example/html_old.xml"

# new sitemap path
NEWSITEMAPPATH = r"/mnt/d/研一/sitemap/example/html.xml"

# 根域名
ROOTURL = "https://tvmchinese.github.io"

# 主页文件名
HOMEPAGE = "index.html"

# Text encodings
ENC_UTF8 = 'UTF-8'
# General Sitemap tags
GENERAL_SITEMAP_TAGS = [
    'loc', 'changefreq', 'priority', 'lastmod'
]

# Match patterns for changefreq attributes
CHANGEFREQ_PATTERNS = [
    'always', 'hourly', 'daily', 'weekly', 'monthly', 'yearly', 'never'
]

# PRIORITIES
PRIORITIES = [
    "1", "0.8", "0.64", "0.51", "0.41", "0.33", "0.26", "0.21"
]

# sitemap namespace
XMLNS = "http://www.sitemaps.org/schemas/sitemap/0.9"

# whether contains .html suffix in url
HTMLSUFFIX = True

# lastmod format can be '%Y-%m-%dT%H:%M:%S+00:00' or '%Y-%m-%d'
LASTMODFORMAT = '%Y-%m-%d'

# log format
LOGGINTFORMAT = '%(asctime)s - %(pathname)s[line:%(lineno)d] - %(levelname)s: %(message)s'

# time zone,北京
TIMEZONE = 8
