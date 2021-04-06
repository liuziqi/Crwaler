import requests

if __name__ == "__main__":
    url = "https://w.wallhaven.cc/full/rd/wallhaven-rddgwm.jpg"

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36 Edg/89.0.774.68"
    }

    # content为获取二进制数据
    img = requests.get(url=url, headers=headers).content

    # wb写入二进制数据
    with open("Resrc/wallpaper.jpg", "wb") as fp:
        fp.write(img)

    print("finish!")
