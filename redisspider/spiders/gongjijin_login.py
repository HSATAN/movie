# -*- coding: utf-8 -*-
from __future__ import print_function

import requests
from PIL import Image
try:
    import cookielib
except:
    import http.cookiejar as cookielib

codeid = '522130199107162455'
password = 'shequ1234'

agent = 'Mozilla/5.0 (Windows NT 5.1; rv:33.0) Gecko/20100101 Firefox/33.0'
headers = {
    "Host": "www.bjrbj.gov.cn",
    "Referer": "http://www.bjrbj.gov.cn/csibiz/indinfo/login.jsp",
    'User-Agent': agent,
    'Connection': 'keep-alive',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8'
}
gongjijin_session = requests.session()
gongjijin_session.cookies = cookielib.LWPCookieJar(filename='gjj_cookies')
try:
    gongjijin_session.cookies.load(ignore_discard=True)
except:
    print('加载gjj_cookie失败')
gongjijin_session.get('http://www.bjrbj.gov.cn/csibiz/indinfo/login.jsp')

def get_image_captcha():
    captcha_url = 'http://www.bjrbj.gov.cn/csibiz/indinfo/validationCodeServlet.do'
    r = gongjijin_session.get(captcha_url)
    with open('gjj_captcha.jpg', 'wb') as f:
        f.write(r.content)
        f.close()

    try:
        im = Image.open('gjj_captcha.jpg')
        im.show()
        im.close()
    except Exception as e:
        print(e)
    captcha = raw_input("please input the captcha>")
    return captcha
def get_phone_captcha():
    url = 'http://www.bjrbj.gov.cn/csibiz/indinfo/passwordSetAction!getTelSafeCode'
    captcha = get_image_captcha()
    data = {
        'idCode': codeid,
        'logPass': password,
        'safeCode': captcha
    }
    print(gongjijin_session.cookies)
    response = gongjijin_session.post(url=url, data=data)
    code = response.text.split('-')[0].strip('"')
    print(response.text)
    return (int(code), captcha)

def login():
    url = 'http://www.bjrbj.gov.cn/csibiz/csiinfo/login_check'

    result = get_phone_captcha()
    phone_number = int(raw_input("请输入手机验证码> "))
    data = {
        'i_username': codeid,
        'i_password': password,
        'safecode': result[1],
        'j_username': codeid,
        'j_password': password,
        'i_safecode': result[1],
        'i_phone': phone_number
    }
    if result[0] in (0, 1):
        r = gongjijin_session.post(url)
        print(r.status_code)
        print(r.text)
        gongjijin_session.cookies.save()

def isLogin():
    pass
login()
# response = gongjijin_session.get('http://www.bjrbj.gov.cn/csibiz/indinfo/menu.jsp?open=null')
# print(response.text)