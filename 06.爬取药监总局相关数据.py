import requests

if __name__ == "__main__":
    url = "http://scxk.nmpa.gov.cn:81/xk/"

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36 Edg/89.0.774.50"
    }

    page_text = requests.get(url=url, headers=headers).text

    with open("./yaojian.html", "w", encoding="utf-8") as fp:
        fp.write(page_text)

