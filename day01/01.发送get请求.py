


import requests

url="http://jy001:8081/futureloan/mvc/api/member/list"

r=requests.get(url)

print(r.text)

assert r.status_code ==200
assert r.reason =="OK"

rjson=r.json()
assert  rjson['status']==1
assert rjson['code']=='10001'
assert rjson["msg"]=="获取用户列表成功"
#响应头
print(r.headers)

url="http://jy001:8081/futureloan/mvc/api/member/register?mobilephone=18010291454&pwd=123456"

r=requests.get(url)
print(r.text)
rjson=r.json()
assert  rjson['status']==1
assert rjson['code']=='10001'
assert rjson["msg"]=="注册成功"






