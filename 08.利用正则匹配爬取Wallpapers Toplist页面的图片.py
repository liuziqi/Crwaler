import requests
import re
import os

if __name__ == "__main__":
    if not os.path.exists("./Wallpapers Toplist"):
        os.mkdir("./Wallpapers Toplist")

    url_Toplist = "https://wallhaven.cc/toplist"

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36 Edg/89.0.774.68"
    }

    pattern = r"<a class=\"preview\" href=\"(.*?)\"  target=\"_blank\"  ></a>"

    # 保存前10页出现的图片
    for i in range(1, 11):
        params = {
            "page": str(i)
        }

        text_Toplist = requests.get(url=url_Toplist, headers=headers, params=params).text

        # re.S 使.匹配包括换行在内的所有字符
        url_list = re.findall(pattern, text_Toplist, re.S)

        pattern_img = r"<img id=\"wallpaper\" src=\"(.*?)\" alt=\".*?</div>"

        for url in url_list:
            text_img = requests.get(url=url, headers=headers).text
            url_img = re.findall(pattern_img, text_img, re.S)[0]
            img = requests.get(url=url_img, headers=headers).content
            name = url_img.split("/")[-1]
            with open("./Wallpapers Toplist/" + name, "wb") as fp:
                fp.write(img)
            print(name + " saved.")

    print("finish!")