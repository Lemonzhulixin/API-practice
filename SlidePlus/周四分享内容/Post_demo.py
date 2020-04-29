#coding=utf-8
import requests
import time

Appkey = 10005300
templeteUrl = "https://t-slide-pre.api.xiaoying.co"
api_ta = "/api/rest/t/ta"
Params_i = "{\"a\":\"zh_CN\"}" #业务参数i

data ={"a":"ta","b":"1.0","c":Appkey,"i":Params_i}  #请求body

responseData = requests.post(templeteUrl + api_ta, data=data)

print(responseData.status_code)
print(responseData.text)




