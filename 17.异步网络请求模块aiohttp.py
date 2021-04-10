import multiprocessing
from flask import Flask
import time
import requests
import asyncio
# 基于异步网络请求的模块
import aiohttp

# 在本地搭了个微服务器
app = Flask(__name__)

def run():
    app.run(threaded=True)

@app.route('/bobo')
def index_bobo():
    time.sleep(2)
    return 'hello bobo'

@app.route('/jay')
def index_jay():
    time.sleep(2)
    return 'hello jay'

@app.route('/tom')
def index_tom():
    time.sleep(2)
    return 'hello tom'

# async定义协程
async def get_page(url):
    print('正在下载', url)
    # request是非异步模块，导致顺序执行
    response = requests.get(url=url)
    print('下载完毕', response.text)

async def get_page_async(url):
    # 异步上下文管理器、
    async with aiohttp.ClientSession() as session:
        # 当在asyncio中遇到了阻塞操作必须进行手动挂起，使用await关键字
        async with await session.get(url=url) as response:
            # 返回二进制形式的响应数据
            # page_text = response.read()
            # 返回json形式的响应数据
            # page_text = response.json()
            # 返回字符串形式的响应数据
            # 注意：在获取响应数据操作之前，一定要使用await手动挂起
            page_text = await response.text()
            print(page_text)

if __name__ == '__main__':
    # 开辟子进程启动服务
    # 不支持自定义对象的序列化
    # 把自定义对象封装到函数里
    app_run = multiprocessing.Process(target=run)
    app_run.start()

    urls = [
        'http://127.0.0.1:5000/bobo',
        'http://127.0.0.1:5000/jay',
        'http://127.0.0.1:5000/tom'
    ]

    tasks = []

    for url in urls:
        cor = get_page(url)
        task = asyncio.ensure_future(cor)
        tasks.append(task)

    loop = asyncio.get_event_loop()
    wait = asyncio.wait(tasks)

    start = time.time()
    # request是非异步模块，导致顺序执行
    loop.run_until_complete(wait)
    end = time.time()
    print('总耗时', end - start, end='\n')


    # aiohttp异步执行
    tasks.clear()

    for url in urls:
        cor = get_page_async(url)
        task = asyncio.ensure_future(cor)
        tasks.append(task)

    loop = asyncio.get_event_loop()
    wait = asyncio.wait(tasks)

    start = time.time()
    # request是非异步模块，导致顺序执行
    loop.run_until_complete(wait)
    end = time.time()
    print('总耗时', end - start, end='\n')


