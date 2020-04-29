import os
import json  # 导入json库
import xlwt  # 导入excel库
import time

file_format = [".json"] #需要查询的文件类型
fileList = [ ]
counter = 0
path = "F:\\SlidePlus\\Report"  #自动化报告json文件路径
now_date = time.strftime("%Y%m%d", time.localtime(time.time()))  # 获取当前时间
json_results = "F:\\SlidePlus\Result\\VivaVideo_signal.xls" #所有接口运行结果写入的Excel文件名称

for files in os.listdir(path):#返回指定目录下的所有文件和目录名
    if files and (os.path.splitext(files)[1] in file_format):  # os.path.splitext():分离文件名与扩展名([0] 文件名，[1]文件扩展名）
       fileList.append(files)
       counter += 1

wb = xlwt.Workbook()  # 创建excel文件
ws = wb.add_sheet(now_date)

i = 0
while i < len(fileList):
   with open("F:\\SlidePlus\\Report\\" + fileList[i], "r", encoding="utf-8-sig") as jsonfile:  # 打开json文件
       print(fileList[i])
       data = json.load(jsonfile)
       jsonData = data["run"]["executions"]

       ws.write(0, 7 * i + 0, "API")
       ws.write(0, 7 * i + 1, "Request URL")
       ws.write(0, 7 * i + 2, "Request Method")
       ws.write(0, 7 * i + 3, "Durition(mms)")
       ws.write(0, 7 * i + 4, "Status Code")
       ws.write(0, 7 * i + 5, "Test Result")
       ws.write(0, 7 * i + 6, "Error Reason")

       a = 1
       while a < len(jsonData):
           try:
               apiName = jsonData[a]["item"]["name"]
               requestUrl = jsonData[a]["item"]["request"]["url"]
               requestMethod = jsonData[a]["item"]["request"]["method"]
               responseTime = jsonData[a]["response"]["responseTime"]
               statusCode = jsonData[a]["response"]["code"]
               testResult = jsonData[a]["response"]["status"]
               responseBody = jsonData[a]["response"]["body"]

               if testResult == "OK":
                   ws.write(a, 7 * i + 0, apiName)
                   ws.write(a, 7 * i + 1, requestUrl)
                   ws.write(a, 7 * i + 2, requestMethod)
                   ws.write(a, 7 * i + 3, responseTime)
                   ws.write(a, 7 * i + 4, statusCode)
                   ws.write(a, 7 * i + 5, testResult)
               else:
                   ws.write(a, 7 * i + 0, apiName)
                   ws.write(a, 7 * i + 1, requestUrl)
                   ws.write(a, 7 * i + 2, requestMethod)
                   ws.write(a, 7 * i + 3, responseTime)
                   ws.write(a, 7 * i + 4, statusCode)
                   ws.write(a, 7 * i + 5, testResult)
                   ws.write(a, 7 * i + 6, responseBody)
                   print(apiName, statusCode, responseBody)
               a = a + 1
           except:
               apiName = jsonData[a]["item"]["name"]
               requestUrl = jsonData[a]["item"]["request"]["url"]
               requestMethod = jsonData[a]["item"]["request"]["method"]
               requestError = jsonData[a]["requestError"]["code"]

               ws.write(a, 7 * i + 0, apiName)
               ws.write(a, 7 * i + 1, requestUrl)
               ws.write(a, 7 * i + 2, requestMethod)
               ws.write(a, 7 * i + 5, "Request Error")
               ws.write(a, 7 * i + 6, requestError)
               print(apiName, requestError)
               a = a + 1
       else:
           print("Create Excel file successed")
       wb.save(json_results)
       i += 1
else:
   print("The end")
