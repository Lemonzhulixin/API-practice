import json  # 导入json库

with open("F:\\SlidePlus\\Report\\" + "reporter_170515_16779.json", "r", encoding="utf-8-sig") as jsonfile:  # 打开json文件
    data = json.load(jsonfile)  # 解码json数据
    jsonData = data["run"]["executions"]
    apiName = jsonData[0]["item"]["name"]
    requestUrl = jsonData[0]["item"]["request"]["url"]
    requestMethod = jsonData[0]["item"]["request"]["method"]
    responseTime = jsonData[0]["response"]["responseTime"]
    statusCode = jsonData[0]["response"]["code"]
    testResult = jsonData[0]["response"]["status"]
    print(apiName,requestUrl,requestMethod,responseTime,statusCode,testResult)