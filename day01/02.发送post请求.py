import requests

#表单格式的数据：content-type:www-x-form-urlencoded



url="http://localhost:8080/carRental/car/addCar.action"

cs={
    'carnumber':'陕A90901',
    'cartype':'大众',
    'color':'黑色',
    'carimg':'images/defaultcarimage.jpg',
    'description':'2020新车',
    'price':900000,
    'rentprice':567890,
    'deposit':123456,
    'isrenting':0
}
#使用脚本添加车辆，中文字符乱码，但使用界面添加，不会有乱码
#分别抓脚本的包与界面的包，对比差异，界面设置了charset=UTF-8，但是脚本未设置导致
head={
    "Content-Type":"application/x-www-form-urlencoded;charset=UTF-8",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"
}
r=requests.post(url,data=cs,headers=head)
print(r.text)






