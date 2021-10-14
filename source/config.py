WORKPATH = "D:\研一\sitemap\sitemap_generator"
ROOTURL = "https://tvmchinese.github.io"
HOMEPAGE = "index.html"
CHANGEFREQ = "weekly"
PRIORITY = 1
# Text encodings
ENC_UTF8 = 'UTF-8'
# General Sitemap tags
GENERAL_SITEMAP_TAGS = ['loc', 'changefreq', 'priority', 'lastmod']

# Match patterns for changefreq attributes
CHANGEFREQ_PATTERNS = [
    'always', 'hourly', 'daily', 'weekly', 'monthly', 'yearly', 'never'
]
# PRIORITIES
PRIORITIES = ["1", "0.8", "0.64", "0.51", "0.41", "0.33", "0.26", "0.21"]
# sitemap header
XMLNS = "http://www.sitemaps.org/schemas/sitemap/0.9"

# whether contains .html suffix in url
HTMLSUFFIX = True
