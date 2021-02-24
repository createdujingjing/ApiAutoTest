import requests

url="http://localhost:8080/carRental/file/uploadFile.action"
file="d:/test.png"
with open(file,mode='rb') as f:
    cs={"mf":(file, f, "img/png")}
    r=requests.post(url,files=cs)

    #"code":0,"msg":"","count":null,"data":{"src":"2021-01-28/202101281448354748352.png_temp"}
    print(r.text)
    uploadPath=r.json()['data']['src']

url = "http://localhost:8080/carRental/car/addCar.action"

cs = {
        'carnumber': '陕A93456',
        'cartype': '大众',
        'color': '黑色',
        'carimg': uploadPath,
        'description': '2020新车',
        'price': 900000,
        'rentprice': 567890,
        'deposit': 123456,
        'isrenting': 0
    }
    # 使用脚本添加车辆，中文字符乱码，但使用界面添加，不会有乱码
    # 分别抓脚本的包与界面的包，对比差异，界面设置了charset=UTF-8，但是脚本未设置导致
head = {
        "Content-Type": "application/x-www-form-urlencoded;charset=UTF-8",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"
    }
r = requests.post(url, data=cs, headers=head)

print(r.text)












