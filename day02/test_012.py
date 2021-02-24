from unittest import mock
#接口地址：http://www.zhifu.com/pay
#方法：post
#
#
#
#

import requests
def zhifu(data):
    print("=====================")
    r=requests.post("http://www.zhifu.com/pay",data)
    return r.json()
def test_zhifu():
    data={"订单号":1232,"支付金额":123,"支付方式":"余额宝"}
    #return_value是参数
    zhifu=mock.Mock(return_value={"code":10001,"msg":"支付成功"})
    r=zhifu(data)
    assert r['msg']=="支付成功"
#模块名.方法名
#模块名.类名.方法名
@mock.patch("test_012.zhifu",return_value={"code": 10001, "msg": "支付成功"})
def test_zhifu2(aa):#这里要传一个参数，虽然参数在内部没有用到
    data = {"订单号": 1232, "支付金额": 123, "支付方式": "余额宝"}
    r = zhifu(data)
    assert r['msg'] == "支付成功"







