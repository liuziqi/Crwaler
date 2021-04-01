import requests
import json

if __name__ == "__main__":
    # 需要明确数据包的链接，参数封装在字典中
    url = "https://movie.douban.com/j/chart/top_list"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36 Edg/89.0.774.50"
    }
    params = {
        "type": "24",
        "interval_id": "100:90",
        "action": "",
        "start": "0",
        "limit": "40"
    }
    response = requests.get(url=url, params=params, headers=headers)
    data = response.json()
    fp = open("./douban.json", 'w', encoding="utf-8")
    json.dump(data, fp=fp, ensure_ascii=False)
    print("finish!")