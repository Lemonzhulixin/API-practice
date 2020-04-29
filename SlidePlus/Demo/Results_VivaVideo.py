import os
import json  # 导入json库
import xlwt  # 导入excel库
import xlrd  #excel扩展库
from xlutils.copy import copy #excel 扩展库

file_format = [".json"] #需要查询的文件类型
fileList = [ ]
counter = 0
path = "F:\\SlidePlus\\Report"  #自动化报告json文件路径
json_results = "F:\\SlidePlus\Result\\VivaVideo_results.xls" #所有接口运行结果写入的Excel文件名称

for files in os.listdir(path):#返回指定目录下的所有文件和目录名
    if files and (os.path.splitext(files)[1] in file_format):  # os.path.splitext():分离文件名与扩展名([0] 文件名，[1]文件扩展名）
       fileList.append(files)
       counter += 1

#读取某一文件夹下所有josn文件并把相应key值写入excel表格中
i = 0
while i < len(fileList):
   with open("F:\\SlidePlus\\Report\\" + fileList[i], "r", encoding="utf-8-sig") as jsonfile:  # 打开json文件
      if os.path.exists(json_results):#判断excel文件是否存在
            print(fileList[i])
            sheet_name = os.path.splitext(fileList[i])[0]
            data = json.load(jsonfile)  # 解码json数据
            jsonData = data["run"]["executions"]
            #length = len(jsonData)  # 获取jsondata数组长度
            oldWb = xlrd.open_workbook(json_results, formatting_info=True)
            newWb = copy(oldWb)
            #newWs = newWb.add_sheet(fileList[i]) #创建sheet带扩展名
            newWs = newWb.add_sheet(sheet_name) #创建sheet无扩展名
            # Excel表格列值
            newWs.write(0, 0, "API")
            newWs.write(0, 1, "Request URL")
            newWs.write(0, 2, "Request Method")
            newWs.write(0, 3, "Durition(mms)")
            newWs.write(0, 4, "Status Code")
            newWs.write(0, 5, "Test Result")
            newWs.write(0, 6, "Error Reason")
            # 读取json数组中的数据
            a = 0
            while a < len(jsonData):
                  try:  # 判断是否有异常的请求
                        apiName = jsonData[a]["item"]["name"]
                        requestUrl = jsonData[a]["item"]["request"]["url"]
                        requestMethod = jsonData[a]["item"]["request"]["method"]
                        responseTime = jsonData[a]["response"]["responseTime"]
                        statusCode = jsonData[a]["response"]["code"]
                        testResult = jsonData[a]["response"]["status"]
                        responseBody = jsonData[a]["response"]["body"]
                        # 获取数据并写入Excel表格中
                        if testResult == "OK" : #判断运行结果是pass or # failed
                              newWs.write(a + 1, 0, apiName)
                              newWs.write(a + 1, 1, requestUrl)
                              newWs.write(a + 1, 2, requestMethod)
                              newWs.write(a + 1, 3, responseTime)
                              newWs.write(a + 1, 4, statusCode)
                              newWs.write(a + 1, 5, testResult)
                        else:
                              newWs.write(a + 1, 0, apiName)
                              newWs.write(a + 1, 1, requestUrl)
                              newWs.write(a + 1, 2, requestMethod)
                              newWs.write(a + 1, 3, responseTime)
                              newWs.write(a + 1, 4, statusCode)
                              newWs.write(a + 1, 5, testResult)
                              newWs.write(a + 1, 6, responseBody)
                              print(apiName, statusCode, responseBody)
                        a = a + 1
                  except:#如果request出错
                        apiName = jsonData[a]["item"]["name"]
                        requestUrl = jsonData[a]["item"]["request"]["url"]
                        requestMethod = jsonData[a]["item"]["request"]["method"]
                        requestError = jsonData[a]["requestError"]["code"]

                        newWs.write(a + 1, 0, apiName)
                        newWs.write(a + 1, 1, requestUrl)
                        newWs.write(a + 1, 2, requestMethod)
                        newWs.write(a + 1, 5, "Request Error")
                        newWs.write(a + 1, 6, requestError)
                        print(apiName, requestError)
                        a = a + 1
            else:
                  print("Read new json file successed")
            newWb.save(json_results)
      else:
            print(fileList[i])
            sheet_name = os.path.splitext(fileList[i])[0]
            data = json.load(jsonfile)
            jsonData = data["run"]["executions"]
            #length = len(jsonData)
            wb = xlwt.Workbook()  # 创建excel文件
            #ws = wb.add_sheet(fileList[i])
            ws = wb.add_sheet(sheet_name)

            ws.write(0, 0, "API")
            ws.write(0, 1, "Request URL")
            ws.write(0, 2, "Request Method")
            ws.write(0, 3, "Durition(mms)")
            ws.write(0, 4, "Status Code")
            ws.write(0, 5, "Test Result")
            ws.write(0, 6, "Error Reason")

            a = 0
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
                              ws.write(a + 1, 0, apiName)
                              ws.write(a + 1, 1, requestUrl)
                              ws.write(a + 1, 2, requestMethod)
                              ws.write(a + 1, 3, responseTime)
                              ws.write(a + 1, 4, statusCode)
                              ws.write(a + 1, 5, testResult)
                        else:
                              ws.write(a + 1, 0, apiName)
                              ws.write(a + 1, 1, requestUrl)
                              ws.write(a + 1, 2, requestMethod)
                              ws.write(a + 1, 3, responseTime)
                              ws.write(a + 1, 4, statusCode)
                              ws.write(a + 1, 5, testResult)
                              ws.write(a + 1, 6, responseBody)
                              print(apiName, statusCode, responseBody)
                        a = a + 1
                  except:
                        apiName = jsonData[a]["item"]["name"]
                        requestUrl = jsonData[a]["item"]["request"]["url"]
                        requestMethod = jsonData[a]["item"]["request"]["method"]
                        requestError = jsonData[a]["requestError"]["code"]

                        ws.write(a + 1, 0, apiName)
                        ws.write(a + 1, 1, requestUrl)
                        ws.write(a + 1, 2, requestMethod)
                        ws.write(a + 1, 5, "Request Error")
                        ws.write(a + 1, 6, requestError)
                        print(apiName, requestError)
                        a =a + 1
            else:
                  print("Create Excel file successed")
            wb.save(json_results)
   i += 1
else:
   print("The end")
