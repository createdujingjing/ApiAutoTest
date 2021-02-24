import requests

url="https://www.bagevent.com/account/dashboard"
r=requests.get(url)
print(r.text)

head={
    "Cookie":'_ga=GA1.2.1869462601.1611729448; _gid=GA1.2.242203481.1611729448; Hm_lvt_1fc37bec18db735c69ebe77d923b3ab9=1611729448; __auc=9ed0738f177428fc15eb0e2f2f8; BAG_EVENT_TOKEN_=02de735f68204d51009e7edda78e58c13a3fcdd1; BAG_EVENT_CK_KEY_="2780487875@qq.com"; BAG_EVENT_CK_TOKEN_=2440f5d17af838308ba4b390db81af38'
}
r=requests.get(url,headers=head)
print(r.text)

assert "<title>百格活动 - 账户总览</title>" in r.text
'''
缺点:
1.cookie会失效，失效后需重新获取
2.登录后的每个接口，需要带着cookie
'''


