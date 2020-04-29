import unittest       #导入unittest
import requests       #导入requests库
import time           #导入time库
import json           #导入json库

class SP_login(unittest.TestCase):              #定义一个类
       def setUp(self):                         #初始化数据
           self.appKey = 10005100
           self.templeteUrl = "https://t-slide.api.xiaoying.co"
           self.pre_templeteUrl = "https://t-slide-pre.api.xiaoying.co"
           self.supportUrl = "https://s-slide.api.xiaoying.co"
           self.pre_supportUrl = "https://s-slide-pre.api.xiaoying.co"
           self.communityUrl = "https://slideplus.api.xiaoying.co"
           self.pre_communityUrl = "https://pe-slideplus.api.xiaoying.co"
           self.deviceId = "647001021469564928"
           self.nowtime = time.strftime("%Y%m%d%H%M%S", time.localtime(time.time()))  # 获取当前时间

       def test_api_aa(self):             #定义一个测试项
           api_aa = "/api/rest/a/aa" #注册
           Params_i = "{\"a\":\"10\",\"b\": \"28DC2123918C8711A253DA1079430419\",\"c\": \"f93b4e0af471d54a36496a0994d84315\"}" #参数i
           data = {"a": "aa", "b": "2.0", "c": self.appKey,"e":self.deviceId,"i": Params_i,"l":self.nowtime}
           responseData = requests.post(self.communityUrl + api_aa, data=data) #POST请求
           self.assertEqual(responseData.status_code,200) #断言返回值是否为200
           #print(responseData.text) #输出返回结果
           data = json.loads(responseData.text) #json数据解码成字符串
           global userCode
           userCode = data["a"]  #获取某一键值
           return userCode

       def test_api_ac(self):
           api_ac = "/api/rest/a/ac" #登录
           Params_i = "{\"a\":\"10\",\"b\": \"28DC2123918C8711A253DA1079430419\",\"c\": \"f93b4e0af471d54a36496a0994d84315\"}"
           data = {"a": "ac", "b": "1.0", "c": self.appKey,"e":self.deviceId,"f":"","i": Params_i,"l":self.nowtime}
           responseData = requests.post(self.communityUrl + api_ac, data=data)
           self.assertEqual(responseData.status_code,200)
           #print(responseData.text)
           data = json.loads(responseData.text)
           global snsToken
           snsToken = data["a"]["a"]
           return snsToken

       def test_api_uc(self):
           api_uc = "/api/rest/u/uc" #用户信息
           Params_i = "{\"a\":\"bedo\"}"
           data = {"a": "uc", "b": "1.0", "c": self.appKey,"e":self.deviceId,"f":self.test_api_aa(),"h":self.test_api_ac(),"i": Params_i,"l":self.nowtime}
           responseData = requests.post(self.communityUrl + api_uc, data=data)
           self.assertEqual(responseData.status_code,200)
           #print(responseData.text)

       def test_api_ad(self):
           api_ad = "/api/rest/a/ad" #登出
           Params_i = "{\"a\":\"10\",\"b\":\"647001021469564928\" }"
           data = {"a": "ad", "b": "1.0", "c": self.appKey,"e":self.deviceId,"f":self.test_api_aa(),"h":self.test_api_ac(),"i": Params_i,"l":self.nowtime}
           responseData = requests.post(self.communityUrl + api_ad, data=data)
           self.assertEqual(responseData.status_code,200)
           #print(responseData.text)