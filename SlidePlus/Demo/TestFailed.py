import json  # 导入json库

with open("F:\\SlidePlus\\Report\\" + "reporter_170518_18314.json", "r", encoding="utf-8-sig") as jsonfile:  # 打开json文件
    data = json.load(jsonfile)  # 解码json数据
    jsonData = data["run"]["executions"]
    length = len(jsonData)  # 获取jsondata数组长度
    # 读取json数组中的数据
    i = 0
    while i < length:
        try:
            apiName = jsonData[i]["item"]["name"]
            requestUrl = jsonData[i]["item"]["request"]["url"]
            requestMethod = jsonData[i]["item"]["request"]["method"]
            responseTime = jsonData[i]["response"]["responseTime"]
            statusCode = jsonData[i]["response"]["code"]
            testResult = jsonData[i]["response"]["status"]
            responseBody = jsonData[i]["response"]["body"]
            #print(apiName, requestUrl, requestMethod, responseTime, statusCode, testResult)
            if testResult == "OK":  # 判断运行结果是pass or # failed
                print("Test OK")
            else:
                print(apiName, statusCode, responseBody)
            i = i + 1
        except:
            apiName = jsonData[i]["item"]["name"]
            requestUrl = jsonData[i]["item"]["request"]["url"]
            requestMethod = jsonData[i]["item"]["request"]["method"]
            requestError = jsonData[i]["requestError"]["code"]
            print(apiName, requestUrl, requestMethod, requestError)
            i = i + 1
    else:
        print("The End")