
import pytest_check as check



def equal(real,expect,keys):
    '''
    assert r.json()['code'] == fail_data['expect']['code']
    assert r.json()['status'] == fail_data['expect']['status']
    assert r.json()['msg'] == fail_data['expect']['msg']
    简化为
    Check.equal(r.json(),fail_data['expect'],'code,status,msg')
    检查两个字典中，key对应的value是否一致
    不推荐直接判等，r.json()==fail_data['expect]
    1.结果中有一些不关键的信息，后面有变化时，回到中脚本执行不通过
    2.结果中有时间戳这类变化信息，每次校验的结果不同，需要变更数据
    :param real:
    :param expect:
    :param keys:
    :return:
    '''
    ks=keys.split(",")#字符串在，处切割
    for k in ks:
        r=str(real[k])#根据k取实际结果中value
        e=str(expect[k])
        try:
            check.equal(r,e)
            print(f"检验{k}成功")
        except Exception as e:
            print(f"检验{k}失败")
