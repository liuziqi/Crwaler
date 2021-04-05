import requests
from lxml import etree
import os

if __name__ == "__main__":
    url_Toplist = "https://wallhaven.cc/toplist"

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36 Edg/89.0.774.68"
    }

    params = {
        "page": "12"
    }

    xml = requests.get(url=url_Toplist, headers=headers, params=params).text

    # parse()方法分析本地文件，HTML()方法分析请求获得的数据
    tree = etree.HTML(xml)

    # /表示一个层级
    # /@attrName获取属性值
    # /text()获取标签直系文本内容
    # //text()或标签下所有文本内容
    urls = tree.xpath("/html/body/main/div/section/ul/li/figure/a/@href")

    # //表示跨越多个层级
    # /*[@id="thumbs"]表示定位到id值为thumbs的标签
    # li[1]表示选择所有符合条件的li标签中的第1个，从1开始计数
    urls = tree.xpath("//*[@id=\"thumbs\"]/section/ul/li/figure/a/@href")

    print(urls)