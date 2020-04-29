# -*- coding: UTF-8 -*-
import MySQLdb
import os
import json  # 导入json库

#连接数据库
conn = MySQLdb.connect(host='localhost', port=3306, user='root', passwd='Zlx123456',charset='utf8') #连接数据库
#conn.set_character_set('utf8') #加上字符集参数，防止中文乱码
cur = conn.cursor() #定义指针
cur.execute('DROP database IF EXISTS vivavideo')
cur.execute('create database if not exists vivavideo')#创建数据库
conn.select_db('vivavideo')
cur.execute('create table results(api varchar(50),url varchar(50),method varchar(50),durition int,code int,status varchar(50))') #创建表格

file_format = [".json"] #需要查询的文件类型
fileList = [ ]
counter = 0
path = "F:\\SlidePlus\\Report"  #自动化报告json文件路径
json_results = "F:\\SlidePlus\Result\\VivaVideo_signal.xls" #所有接口运行结果写入的Excel文件名称

for files in os.listdir(path):#返回指定目录下的所有文件和目录名
    if files and (os.path.splitext(files)[1] in file_format):  # os.path.splitext():分离文件名与扩展名([0] 文件名，[1]文件扩展名）
       fileList.append(files)
       counter += 1

i = 0
while i < len(fileList):
   with open("F:\\SlidePlus\\Report\\" + fileList[i], "r", encoding="utf-8-sig") as jsonfile:  # 打开json文件
       print(fileList[i])
       data = json.load(jsonfile)
       jsonData = data["run"]["executions"]
       a = 1
       while a < len(jsonData):
           try:
               apiName = jsonData[a]["item"]["name"]
               requestUrl = jsonData[a]["item"]["request"]["url"]
               requestMethod = jsonData[a]["item"]["request"]["method"]
               responseTime = jsonData[a]["response"]["responseTime"]
               statusCode = jsonData[a]["response"]["code"]
               testResult = jsonData[a]["response"]["status"]

               value = [apiName, requestUrl, requestMethod, responseTime, statusCode, testResult]
               cur.execute('insert into results values(%s,%s,%s,%s,%s,%s)', value)#写入数据库
               conn.commit()#提交写入内容
               a = a + 1
           except:
               apiName = jsonData[a]["item"]["name"]
               requestUrl = jsonData[a]["item"]["request"]["url"]
               requestMethod = jsonData[a]["item"]["request"]["method"]
               requestError = jsonData[a]["requestError"]["code"]

               value = [apiName, requestUrl, requestMethod, 0, 0, requestError]
               cur.execute('insert into results values(%s,%s,%s,%s,%s,%s)', value)
               conn.commit()
               a = a + 1
       else:
           print(fileList[i] + ":OK")
   i = i + 1
else:
    print("The end")
cur.close()
conn.close()#关闭连接










