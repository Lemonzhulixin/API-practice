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
           self.nowtime = time.strftime("%Y%m%d%H%M%S", time.localtime(time.time()))  # 获取当前时间（currentime）

       def test_api_aa(self):             #定义一个测试项
           api_aa = "/api/rest/a/aa" #注册
           Params_i = "{\"a\":\"10\",\"b\": \"28DC2123918C8711A253DA1079430419\",\"c\": \"f93b4e0af471d54a36496a0994d84315\"}" #参数i
           data = {"a": "aa", "b": "2.0", "c": self.appKey,"e":self.deviceId,"i": Params_i,"l":self.nowtime}
           responseData = requests.post(self.communityUrl + api_aa, data=data) #POST请求
           self.assertEqual(responseData.status_code,200) #断言返回值是否为200
           print(responseData.text) #输出返回结果
           data = json.loads(responseData.text) #json数据解码成字符串
           #print(data)
           #data1 = json.dumps(data)
           #print(data1)
           global userCode
           userCode = data["a"]  #获取某一键值
           #print(userCode)
           return userCode

#1. currenttime  2.获取某一key对应的值并返回该值