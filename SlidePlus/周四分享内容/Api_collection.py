import xlwt  #导入excel库
import xlrd  #导入Excel的扩展工具库

json_results = "F:\\SlidePlus\Result\\VivaVideo_results.xls" #所有接口运行结果写入的Excel文件名称
api_results = "F:\\SlidePlus\Result\\Map_VivaVideo_api.xls" #单个接口所有运行结果写入的Excel文件名称
file = xlrd.open_workbook(json_results)#打开VivaVideo_results.xls
api_wb = xlwt.Workbook()  # 创建新的excel文件
api_ws = api_wb.add_sheet("Templete API")  # 创建sheet
# 新sheet的表格列值
api_ws.write(0, 0, "API")
api_ws.write(0, 1, "Request URL")
api_ws.write(0, 2, "Request Method")
api_ws.write(0, 3, "Durition(mms)")
api_ws.write(0, 4, "Status Code")
api_ws.write(0, 5, "Test Result")

# 获取所要展示的接口对应数据
i = 0
while i < len(file.sheets()):
      sheet_name = file.sheet_names()[i] #遍历VivaVideo_results.xls中sheet名称
      try:
          sheet = file.sheet_by_name(sheet_name)
      except:
          print("No sheet in %s named %s" % (json_results,sheet_name))

      #读取VivaVideo_results.xls中每个sheet中的某一行数据
      api_rows = 1 #此示例展示“Router-获取不同地区的域名接口”返回的数据
      apiName = sheet.cell_value(api_rows, 0)
      requestUrl = sheet.cell_value(api_rows, 1)
      requestMethod = sheet.cell_value(api_rows, 2)
      responseTime = sheet.cell_value(api_rows, 3)
      statusCode = sheet.cell_value(api_rows, 4)
      testResult = sheet.cell_value(api_rows, 5)

      #把获取的数据写入VivaVideo_api.xls
      api_ws.write(i + 1, 0, apiName)
      api_ws.write(i + 1, 1, requestUrl)
      api_ws.write(i + 1, 2, requestMethod)
      api_ws.write(i + 1, 3, responseTime)
      api_ws.write(i + 1, 4, statusCode)
      api_ws.write(i + 1, 5, testResult)
      i = i + 1
else:
    print("No more sheet")
api_wb.save(api_results) #保存所有获取的数据到VivaVideo_api.xls