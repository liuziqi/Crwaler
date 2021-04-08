import asyncio

# async定义协程
async def request(url):
    print('正在请求的url是', url)
    print('请求成功', url)
    return url

if __name__ == '__main__':
    # 返回一个协程对象，不会立即执行
    cor = request('www.baidu.com')
    # 创建一个事件循环对象
    loop = asyncio.get_event_loop()
    # 将协程对象注册到loop中，然后启动loop
    loop.run_until_complete(cor)
    print()

    # task是对协程对象的封装
    loop = asyncio.get_event_loop()
    # 基于loop创建了一个task对象
    cor = request('www.google.com')
    task = loop.create_task(cor)
    print(task)
    # 启动loop
    loop.run_until_complete(task)
    print(task)
    print()

    # feature和task都是协程对象的封装，没有本质区别
    # task基于事件循环创建，feature不是
    loop = asyncio.get_event_loop()
    cor = request('www.bilibili.com')
    task = asyncio.ensure_future(cor)
    print(task)
    loop.run_until_complete(task)
    print(task)
    print()

    # 定义回调函数
    def callback_func(task):
        # result返回的就是协程对象对应函数（request函数）的返回值
        print(task.result())

    # 绑定回调
    cor = request('www.bilibili.com')
    task = asyncio.ensure_future(cor)
    loop = asyncio.get_event_loop()
    # 绑定回调函数到任务对象，将task作为callback_func的参数
    task.add_done_callback(callback_func)
    loop.run_until_complete(task)





