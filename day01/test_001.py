import requests
def test_register_001():
    url = "http://jy001:8081/futureloan/mvc/api/member/register"
    r = requests.get(url)
    print(r.text)
    assert r.status_code == 200
    assert r.reason == "OK"
    print("注册成功的脚本")

def test_register1_002():
    url = "http://jy001:8081/futureloan/mvc/api/member/register"
    cs={
        "mobilephone":1802020908,
        "pwd":123456,
        "regname":'m'
    }
    r = requests.get(url,data=cs)
    print(r.text)
    assert r.status_code == 200
    assert r.reason == "OK"
    print("手机号已被注册")

def test_register2_003():
    url = "http://jy001:8081/futureloan/mvc/api/member/register"
    cs={
        "mobilephone":1802020908,
        "pwd":12345,
        "regname":'m'
    }
    r = requests.get(url,data=cs)
    print(r.text)
    assert r.status_code == 200
    assert r.reason == "OK"
    print("密码少于6位")

def test_register3_004():
    url = "http://jy001:8081/futureloan/mvc/api/member/register"
    cs={
        "mobilephone":"",
        "pwd":12345,
        "regname":'m'
    }
    r = requests.get(url,data=cs)
    print(r.text)
    assert r.status_code == 200
    assert r.reason == "OK"
    print("手机号未填，注册失败")

def test_register4_005():
    url = "http://jy001:8081/futureloan/mvc/api/member/register"
    cs={
        "mobilephone":"",
        "pwd":"",
        "regname":'m'
    }
    r = requests.get(url,data=cs)
    print(r.text)
    assert r.status_code == 200
    assert r.reason == "OK"
    print("手机号，密码必填")

def test_login_006():
    url = "http://jy001:8081/futureloan/mvc/api/member/login"
    r = requests.get(url)
    print(r.text)
    assert r.status_code == 200
    assert r.reason == "OK"
    print("登录成功的脚本")

def test_login1_007():
    url = "http://jy001:8081/futureloan/mvc/api/member/login"
    cs={
        "mobilephone":18023456787,
        "pwd":123456
    }
    r = requests.get(url,data=cs)
    print(r.text)
    assert r.status_code == 200
    assert r.reason == "OK"
    print("手机号不一致")
def test_login2_008():
    url = "http://jy001:8081/futureloan/mvc/api/member/login"
    cs={
        "mobilephone":1802020908,
        "pwd":1234567
    }
    r = requests.get(url,data=cs)
    print(r.text)
    assert r.status_code == 200
    assert r.reason == "OK"
    print("密码错误")

