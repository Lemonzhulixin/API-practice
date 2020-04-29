import requests

Appkey = 10005300   #Appkey
supportUrl = "http://s-slide-pre.api.xiaoying.co" #请求域名
api_imageconfig = "/api/rest/s/imageconfig"  #方法名

requestParam_cn = "{\"b\":\"zh_CN\",\"c\":\"CN\"}"

head = {"Content-Type":"application/x-www-form-urlencoded","X-Forwarded-For":"115.197.180.232" }

params ={"serverVer":"1.0","appKey":Appkey,"requestParam":requestParam_cn}

getData = requests.get(supportUrl + api_imageconfig, params=params,headers=head)  #请求url

print(getData.status_code)
print(getData.url)
print(getData.)


