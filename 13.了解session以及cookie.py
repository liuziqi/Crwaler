import requests
from lxml import etree
from VeriCodeRecognition import VCR
import Password

if __name__ == '__main__':
    # 古诗文网登录页面
    url = 'https://so.gushiwen.cn/user/login.aspx?from=http://so.gushiwen.cn/user/collect.aspx'

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36 Edg/89.0.774.68'
    }

    # Session可以保存当前状态(cookie)
    session = requests.Session()
    xml = session.get(url=url, headers=headers).text

    tree = etree.HTML(xml)
    # 验证码图片url
    code_url = 'https://so.gushiwen.cn' + tree.xpath('//*[@id="imgCode"]/@src')[0]

    code_im = session.get(url=code_url, headers=headers).content
    code = VCR().PostPic(im=code_im, codetype=1902)['pic_str']
    print('code:', code)

    with open('./Resrc/code_im.jpg', 'wb') as fp:
        fp.write(code_im)

    login_url = 'https://so.gushiwen.cn/user/login.aspx?from=http%3a%2f%2fso.gushiwen.cn%2fuser%2fcollect.aspx'

    params = {
        '__VIEWSTATE': '76C9TVjnJz+VuVOIpvbDa6FR8mNKSq/SR46/O8/xsGZd6bDEZZnSt2ujbbLg/04i/cBF56i4owXymZpp3WXcr5iu9bdd3b5kEXT5mbLTru6Q5wzjNIlvuG2JaPw=',
        '__VIEWSTATEGENERATOR': 'C93BE1AE',
        'from': 'http://so.gushiwen.cn/user/collect.aspx',
        'email': Password.gushiwen_email,
        'pwd': Password.gushiwen_pwd,
        'code': code,
        'denglu': '登录'
    }

    # 状态码200，手动访问时状态码302，是否发生重定向？
    response = session.post(url=login_url, headers=headers, params=params)
    print('status code:', response.status_code)

    # 个人中心页面
    me_url = 'https://so.gushiwen.cn/user/collect.aspx'
    response = session.get(url=me_url, headers=headers)
    xml = response.text

    # 登陆成功了，偶尔失败是因为验证码识别错误
    with open('./Resrc/gushiwen2.html', 'w', encoding='utf-8') as fp:
        fp.write(xml)