import requests
import json

if __name__ == "__main__":
    # 爬取前10页的公司ID
    url = "http://scxk.nmpa.gov.cn:81/xk/itownet/portalAction.do?method=getXkzsList"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36 Edg/89.0.774.50"
    }

    ID = []

    for i in range(10):
        params = {
            "on": "true",
            "page": str(i+1),
            "pageSize": "15",
            "productName": "",
            "conditionType": "1",
            "applyname": "",
            "applysn": ""
        }
        page_json = requests.post(url=url, headers=headers, params=params).json()

        for j in range(len(page_json["list"])):
            ID.append(page_json["list"][j]["ID"])

    # 根据id爬取公司信息
    url = "http://scxk.nmpa.gov.cn:81/xk/itownet/portalAction.do?method=getXkzsById"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36 Edg/89.0.774.50"
    }

    info = []

    for id in ID:
        params = {
            "id": id
        }
        page_json = requests.post(url=url, headers=headers, params=params).json()
        info.append(page_json)

    print(info)
    print(len(info))

    # 持久化存储
    with open("./yjzj_data.json", "w", encoding="utf-8") as fp:
        # ensure_ascii=False，否则会保存成ascii码
        json.dump(info, fp=fp, ensure_ascii=False)

