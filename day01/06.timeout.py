'''
1.上传文件的接口，上传1M文件时，默认超时时间不够用，可设置接口超时时间
2.接口性能测试，看接口是否能在某个时间内返回
'''

import requests
for i in range(10):
    try:
        r = requests.get("http://jy001:8081/futureloan/mvc/api/member/list", timeout=0.1)
        print(r.text)
    except Exception as e:
        print(e)








