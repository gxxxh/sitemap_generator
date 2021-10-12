from lxml import etree
# html字符串





if __name__ == "__main__":
    html_str = """
    <html>
    <head>
    <title>demo</title>
    </head>
    <body>
    <p>1111111</p>
    </body>
    </html>
    """
    html = etree.HTML(html_str)
    type(html)  # 输出结果为：lxml.etree._Element