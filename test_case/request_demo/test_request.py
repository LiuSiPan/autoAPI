import allure
import requests


@allure.feature("请求")
@allure.story("模块")
@allure.title("用例名")
def test_no_params(pub_data):
    # 发送无参数的get请求, 尝试获取某个网页.
    with allure.step("第一步：请求数据"):pass
    r1 = requests.get("https://www.baidu.com/")
    print(r1)

    # 发送无参数的get请求设置超时时间timeout单位秒
    with allure.step("第二步：请求数据"): pass
    with allure.step("第三步：请求数据"):
        allure.attach("请求行，请求头，请求正文","请求信息",allure.attachment_type.TEXT)
    r2 = requests.get('http://www.baidu.com', timeout=1)
    print(r2)

def test_has_params():
    payload = {'key1': 'value1', 'key2': 'value2'}
    r = requests.get("https://www.baidu.com/", params=payload)
    print(r.url)
    # https: // www.baidu.com /?key2 = value2 & key1 = value1

    payload = {'key1': 'value1', 'key2': ['value2', 'value3']}
    r = requests.get('http://www.baidu.com/', params=payload)
    print(r.url)
    # http: // www.baidu.com /?key2 = value2 & key2 = value3 & key1 = value1

def test_head_has_params():
    # 定制请求头,如果你想为请求添加 HTTP 头部，只要简单地传递一个 dict 给 headers 参数就可以了
    url = 'https://www.baidu.com/s?wd=python'
    headers = {
        'Content-Type': 'text/html;charset=utf-8',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
    }
    r = requests.get(url, headers=headers)
    print(r.url)


def test_form_post_params():
    # 1.以form形式发送post请求,Reqeusts支持以form表单形式发送post请求，只需要将请求的参数构造成一个字典，然后传给requests.post()的data参数即可
    payload = {'key1': 'value1',
               'key2': 'value2'
               }
    r = requests.post("http://httpbin.org/post", data=payload)
    print(r.text)

def test_json_post_params():
    # 2.以json形式发送post请求
    # 可以将一 json串传给requests.post()的data参数，
    payload = {'key1': 'value1',
               'key2': 'value2'
               }
    r = requests.post("http://httpbin.org/post", json=payload)
    print(r.text)

def test_post_json():
    payload = {'pwd': 'abc123',
               'userName': 'tuu653'
               }
    r = requests.post("http://qa.yansl.com:8084/login", json=payload)
    print(r.text)

def test_post_form(pub_data):
    payload = {'userName': 'tuu653'
               }
    h = {"token":pub_data["token"]}
    print(h)
    r = requests.post("http://qa.yansl.com:8084/user/lock", data=payload,headers=h)
    print(r.text)

def test_post_upload_file(pub_data):
    data = {
        "file":open("hhh.xls","rb")
    }
    h = {"token":pub_data["token"]}
    r = requests.post("http://qa.yansl.com:8084/product/uploaProdRepertory", files=data, headers=h)
    print(r.text)




