import pytest
import requests

cs = {
    #密码少于6位
    {"data":{"mobilephone": 1802020908, "pwd": "12345", "regname": 'm'},
     "except":{"status":0,"code":20108,"data":None,"msg":"密码长度为6-18位"}},

    # 密码大于18位
    {"data": {"mobilephone": 1802020908, "pwd": "12345678901234567890", "regname": 'm'},
     "except": {"status": 0, "code": 20109, "data": None, "msg": "密码长度为6-18位"}},

}

@pytest.fixture(params=cs)
def login_data(request):  # 固定写法，request是pytest中的关键字
    return request.param  # 固定写法
def register(data):
    url = "http://jy001:8081/futureloan/mvc/api/member/register"
    r=requests.post(url,data=data)
    return r
#数据驱动的测试模型
#test_register测试脚本/测试逻辑，测试数据与测试逻辑分离，相同逻辑的数据放在一起
#数据可以放在csv、xml、yaml.....去维护
def test_register(register_data):
    print(f"测试数据：{register_data['data']}")
    print(f"预期结果：{register_data['except']}")
    r=register(register_data['data'])
    print(f"实际结果：{r.text}")
    assert r.json()['status']==register_data['expect']['status']
    assert r.json()['code']==register_data['expect']['code']
    assert r.json()['msg']==register_data['expect']['msg']


