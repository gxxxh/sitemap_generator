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


## example
1. index.html文件内容修改
2. 新增了release_process.html
3. 删除了pull_request.html

## 参考
[google sitemap](https://www.cnblogs.com/doinbean/p/8488466.html)
[Sitemaps XML format](https://www.sitemaps.org/protocol.html)