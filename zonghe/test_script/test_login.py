import pytest

from zonghe.baw import Member
from zonghe.caw import DataRead, MySqlOp


@pytest.fixture(params=DataRead.read_yaml(r"test_data\login_setup.yaml"))
def setup_data(request):
    return request.param

@pytest.fixture(params=DataRead.read_yaml(r"test_data\login_data.yaml"))
def login_data(request):
    return request.param


@pytest.fixture()
def register(setup_data,baserequest,url,db_info):
    #初始化
    MySqlOp.delete_user(db_info, setup_data['data']['mobilephone'])

    #注册用户
    r = Member.register(baserequest,url,setup_data['data'])
    yield

    #删除注册用户
    MySqlOp.delete_user(db_info, setup_data['data']['mobilephone'])



def test_login(register,login_data,baserequest,url):
    print(login_data)
    #下发登录的请求
    r = Member.login(baserequest,url,login_data['data'])
    #检查结果
    assert r.json()['code'] == login_data['expect']['code']
    assert r.json()['status'] == login_data['expect']['status']
    assert r.json()['msg'] == login_data['expect']['msg']