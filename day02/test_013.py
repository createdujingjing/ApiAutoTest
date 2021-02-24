from unittest import mock

import requests
def chongzhi(data):
    print("=====================")
    r=requests.post("/jy001:8081/futureloan/mvc/api/member/recharge",data)
    return r.json()
def test_chongzhi():
    data={"手机号":1802020908,"amount":1000}
    #return_value是参数
    chongzhi=mock.Mock(return_value={"code":10001,"status":"1"})
    r=chongzhi(data)
    assert r['msg']=="充值成功"

def quxian(data):
    print("=====================")
    r=requests.post("/jy001:8081/futureloan/mvc/api/member/recharge",data)
    return r.json()
def test_chongzhi():
    data={"手机号":1802020908,"amount":1000}
    #return_value是参数
    chongzhi=mock.Mock(return_value={"code":10001,"status":"1"})
    r=chongzhi(data)
    assert r['msg']=="充值成功"

