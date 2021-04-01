import requests
import json

if __name__ == "__main__":
    # 发起请求后页面不跳转为ajax请求，XHR中查看数据包
    url = "https://fanyi.baidu.com/sug"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36 Edg/89.0.774.50"
    }
    # post请求参数
    word = input("enter a word: ")
    data = {
        "kw": word
    }
    response = requests.post(url=url, data=data, headers=headers)
    # 返回字典对象（确认服务器以json类型响应）
    dic = response.json()
    print(dic)
    # 存储json文件
    file_name = word + ".json"
    fp = open(file_name, 'w', encoding="utf-8")
    json.dump(dic, fp=fp, ensure_ascii=False)
    print(file_name + " saved!")
