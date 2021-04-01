import requests

if __name__ == "__main__":
    url = "https://www.sogou.com/web"
    # UA伪装，将对应的User-Agent封装到字典中
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36 Edg/89.0.774.50"
    }
    kw = input("enter a key word: ")
    param = {
        "query": kw
    }
    # 携带参数的get请求
    response = requests.get(url=url, params=param, headers=headers)
    page_text = response.text
    file_name = kw + ".html"
    with open(file_name, 'w', encoding="utf-8") as fp:
        fp.write(page_text)
    print(file_name + " saved!")