import requests
from lxml import etree
import os

if __name__ == '__main__':
    url = "https://cd.58.com/ershoufang/"

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36 Edg/89.0.774.68"
    }

    xml =  requests.get(url=url, headers=headers).text

    tree = etree.HTML(xml)

    tags = tree.xpath('//section[@class="list"]//div[@class="property-content"]')

    for div in tags:
        # ./表示在当前路径下查找标签
        title = div.xpath('.//div[@class="property-content-title"]/h3/@title')[0]
        price = div.xpath('.//span[@class="property-price-total-num"]/text()')[0]
        unit = div.xpath('.//span[@class="property-price-total-text"]/text()')[0]
        print(title, price, unit)
