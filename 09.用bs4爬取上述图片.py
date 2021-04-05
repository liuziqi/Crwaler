import requests
from bs4 import BeautifulSoup
import os

if __name__ == "__main__":
    if not os.path.exists("./Wallpapers Toplist"):
        os.mkdir("./Wallpapers Toplist")

    url_Toplist = "https://wallhaven.cc/toplist"

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36 Edg/89.0.774.68"
    }

    # 爬取第11页的图片
    params = {
        "page": "11"
    }

    xml = requests.get(url=url_Toplist, headers=headers, params=params).text

    # 构造bs类对象
    soup = BeautifulSoup(xml, "lxml")

    # 查找第一个li标签
    soup.li
    soup.find("li")

    # 查找所有li标签
    soup.find_all("li")

    # 查找所有a标签，class属性为preview
    tags = soup.find_all("a", class_="preview")

    # 选择(id, class)属性为preview的标签，返回一个列表
    soup.select(".preview")

    # select作为层级选择器
    # > 表示一个层级，层层递进找到所有满足条件的a标签
    soup.select("main > div > section > ul > li > figure > a")
    # 空格表示多个层级
    soup.select("main  ul figure a")

    # 获取标签之间的文本数据
    # soup.a.text / soup.a.string / soup.a.get_text()
    # text / get_text() 获取某一标签中所有文本内容（包括其子标签中的文本）
    # string 只获取当前标签下直系文本内容

    # 获取标签属性值
    urls = [tag["href"] for tag in tags]

    # 获取每张图片的url
    for url in urls:
        xml = requests.get(url=url, headers=headers).text
        soup = BeautifulSoup(xml, "lxml")
        src = soup.select("main > section > div > img")[0]["src"]
        img = requests.get(url=src, headers=headers).content
        name = src.split("/")[-1]
        with open("./Wallpapers Toplist/" + name, "wb") as fp:
            fp.write(img)
        print(name + " saved.")

    print("finish!")
