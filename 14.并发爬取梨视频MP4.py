import requests
from lxml import etree
import os
from multiprocessing import Pool
import re

session = requests.Session()

def download_video(info_dic):
    url = info_dic['url']
    name = info_dic['name']

    print(name, '正在下载')

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36 Edg/89.0.774.68'
    }

    video = session.get(url=url, headers=headers).content

    if not os.path.exists('./Pear Video'):
        os.mkdir('./Pear Video')

    with open('./Pear Video/' + name, 'wb') as fp:
        fp.write(video)

    print(name, '下载成功。')


if __name__ == '__main__':
    # 梨视频生活板块视频页的链接
    host_url = 'https://www.pearvideo.com/category_5'

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36 Edg/89.0.774.68'
    }

    xml = session.get(url=host_url, headers=headers).text

    tree = etree.HTML(xml)

    video_info_li_list = tree.xpath('//*[@id="listvideoListUl"]/li')

    video_info = []

    for li in video_info_li_list:

        video_id = li.xpath('./div/a/@href')[0].split('_')[-1]

        video_name = li.xpath('./div/a/div[2]/text()')[0] + '.mp4'

        video_info_dic = {
            'id': video_id,
            'name': video_name,
            'url': ''
        }

        video_info.append(video_info_dic)

    # 用于动态获取视频资源的url
    video_query_url = 'https://www.pearvideo.com/videoStatus.jsp'

    for info in video_info:

        video_query_headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36 Edg/89.0.774.68',
            'Referer': 'https://www.pearvideo.com/video_' + info['id']
        }

        params = {
            'contId': info['id'],
            'mrd': '0.6133240947609502'
        }

        # 通过ajax请求动态获取视频url
        video_json = session.get(url=video_query_url, headers=video_query_headers, params=params).json()

        # 该链接不正确，需要处理
        confused_url = video_json['videoInfo']['videos']['srcUrl']

        # 用正则表达式找到待替换的子串
        ex = 'https://video.pearvideo.com/mp4/.*?/.*?/(.*?)-.*?.mp4'

        for_replace = re.findall(ex, confused_url)[0]

        info['url'] = confused_url.replace(for_replace, 'cont-' + info['id'])

    print(video_info)

    # 最大线程数4
    pool = Pool(4)

    pool.map(download_video, video_info)

    pool.close()

    pool.join()







