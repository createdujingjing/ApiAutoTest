'''
fixure带参数
'''

import pytest
#5组测试数据，表示不同的用户名
@pytest.fixture(params=["root","admin","123","Test-345","administrator"])
def login_data(request):#固定写法，request是pytest中的关键字
    return request.param #固定写法


#使用5组数据分别执行这个用例，共执行5次
def test_login(login_data):
    print(f"测试登录功能，使用用户名：{login_data}登录")


@pytest.fixture(params=[{"username":"root","pwd":"123456"},{"username":"Test-345","pwd":"123456"}])
def login_data2(request):#固定写法，request是pytest中的关键字
    return request.param #固定写法


def test_login2(login_data2):
    print(f"测试登录功能，使用用户名：{login_data2['username']},密码：{login_data2['pwd']}登录")














