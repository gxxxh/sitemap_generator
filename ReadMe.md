## SiteMap
最简单的sitemap就是xml文件，在其中列出网站中的网址以及关于每个网址的其他元数据（上次更新的时间、更改的频率以及相对于网站上其他网址的重要程度为何等），以便搜索引擎可以更加智能地抓取网站。

## google sitemap
### 标签
1. urlset 定义了此xml文件的命名空间，相当于网页文件中的<html>标签一样的作用
	1. url 链接定义
		* loc 链接地址，链接地址中的一些特殊字符必须转换为XML(HTML)定义的转义字符
		* changefreq 更新频率
		* lastmod 页面最后修改时间
		* priority 索引优先权，0-1z之间

### 举例
```
<urlset xmlns=“网页列表地址”>
    <url>
        <loc>网址</loc>
        <lastmod>2005-06-03T04:20-08:00</lastmod>
        <changefreq>always</changefreq>
        <priority>1.0</priority>
    </url>
    <url>
        <loc>网址</loc>
        <lastmod>2005-06-02T20:20:36Z</lastmod>
        <changefreq>daily</changefreq>
        <priority>0.8</priority>
    </url>
</urlset>
```


## 使用
### 使用方式
1. 通过单个html文件夹创建sitemap
```
	dir_path = HTMLPATH
    sitemap = DirToSitemap(dir=dir_path, html=HTMLSUFFIX, root_url=ROOTURL, home_page=HOMEPAGE,
                           change_freq=CHANGEFREQ_PATTERNS[3], nsmap=XMLNS, priorities=PRIORITIES, time_zone=TIMEZONE,
                           time_pattern=LASTMODFORMAT)
    # sitemap.add_homepage()
    pt = sitemap.parse_dir("")
    pt.sort()
    pt.save(NEWSITEMAPPATH)
```
2. 对比html_old和html生成新的sitemap
```
    html = HTMLPATH
    html_old = HTMLOLDPATH
    old_sitemap = OLDSITEMAPPATH
    pt = compare(html_old, html, old_sitemap)
    pt.sort()
    pt.save(NEWSITEMAPPATH)
```

### 参数说明(修改config.py中参数)
1. HTMLPATH: 文件夹html的绝对路径
2. HTMLOLDPATH: 文件夹html_old的绝对路径
3. OLDSITEMAPPATH: sitemap_old的绝对路径
4. NEWSITEMAPPATH: 生成sitemap的存储路径
5. ROOTURL: html对应网页的根域名
6. HOMEPAGE：网页主页对应的html文件名
7. HTMLSUFFIX: 生成sitemap中url是否包含.html后缀
8. ENC_UTF8：sitemap编码方式
9. CHANGEFREQ_PATTERNS：changefreq可选参数
10. PRIORITIES: sitemap 优先级设置（对应文件在目录中的深度），主页优先级为1.0
11. XMLNS: sitemap的namespace
12. LASTMODFORMAT: lastmod字符串格式
13. TIMEZONE: 时区


## 参考
1. [google sitemap](https://developers.google.com/search/docs/advanced/sitemaps/build-sitemap)
2. [Sitemaps XML format](https://www.sitemaps.org/protocol.html)
3. [python lxml](https://lxml.de/3.8/index.html)
4. [sitemap validator](https://www.mysitemapgenerator.com/service/check.html)