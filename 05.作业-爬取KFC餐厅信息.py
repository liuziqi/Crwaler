import requests

if __name__ == "__main__":
    url =  "http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=keyword"
    headers = {
        "User-Agent": "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36 Edg/89.0.774.50"
    }
    page = [1, 2, 3]
    for p in page:
        params = {
            "cname": '',
            "pid": '',
            "keyword": "成都",
            "pageIndex": str(p),
            "pageSize": "10"
        }
        # 请求空页面只会返回空数据，不会报错
        try:
            response = requests.post(url=url, headers=headers, params=params)
            print(response.text)
        except:
            print("page " + str(p) + " error!")
    print("finish!")