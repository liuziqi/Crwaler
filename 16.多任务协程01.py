import asyncio
import time

async def request(url):
    print('正在下载', url)

    # 同步模块
    # 在异步协程中如果出现了同步模块相关的代码，那么就无法实现异步
    # time.sleep(2)

    # 异步模块
    # 当在asyncio中遇到了阻塞操作必须进行手动挂起，await关键字
    await asyncio.sleep(2)

    print('下载完毕', url)

if __name__ == '__main__':
    urls = [
        'www.baidu.com',
        'www.sogou.com',
        'www.goubanjia.com'
    ]

    # 任务列表，存放多个任务对象
    tasks_list = []

    for url in urls:
        cor = request(url)
        task = asyncio.ensure_future(cor)
        tasks_list.append(task)

    loop = asyncio.get_event_loop()
    # 将任务列表封装到asyncio.wait()中
    wait = asyncio.wait(tasks_list)

    # 开始时间
    start = time.time()

    # 将任务列表注册到事件循环
    loop.run_until_complete(wait)

    # 所有协程结束时间
    end = time.time()

    # 非异步顺序执行，每个2s，总共用时6s
    print(end - start)