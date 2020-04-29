import xlwt  #导入excel库
import xlrd  #导入Excel的扩展工具库
import time
#导入绘图库
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.pyplot import savefig

json_results = "F:\\SlidePlus\Result\\VivaVideo_signal.xls" #所有接口运行结果写入的Excel文件名称
api_results = "F:\\SlidePlus\Result\\Map_VivaVideo_api.xls" #单个接口所有运行结果写入的Excel文件名称
now_time = time.strftime("%Y%m%d%H%M%S", time.localtime(time.time()))  # 获取当前时间

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

sheet_name = file.sheet_names()[0] #获取VivaVideo_signal.xls中sheet名称
sheet = file.sheet_by_name(sheet_name)

count_cols = sheet.ncols  # 获取列数
length = count_cols/7
api_rows = 2 #所有查看的接口所在行数
i = 0
while i < length:
    #某一行所有值
    apiName = sheet.cell_value(api_rows, 7 * i + 0)
    requestUrl = sheet.cell_value(api_rows, 7 * i + 1)
    requestMethod = sheet.cell_value(api_rows, 7 * i + 2)
    responseTime = sheet.cell_value(api_rows, 7 * i + 3)
    statusCode = sheet.cell_value(api_rows, 7 * i + 4)
    testResult = sheet.cell_value(api_rows, 7 * i + 5)

    # 把获取的数据写入VivaVideo_api.xls
    api_ws.write(i + 1, 0, apiName)
    api_ws.write(i + 1, 1, requestUrl)
    api_ws.write(i + 1, 2, requestMethod)
    api_ws.write(i + 1, 3, responseTime)
    api_ws.write(i + 1, 4, statusCode)
    api_ws.write(i + 1, 5, testResult)
    i = i + 1
else:
    print("No more sheet")
api_wb.save(api_results)  # 保存所有获取的数据到Map_VivaVideo_api.xls

#绘制折线图
api_file = xlrd.open_workbook(api_results) #打开VivaVideo_api.xls
#读取VivaVideo_api.xls sheet名称
sheet_name = api_file.sheet_names()[0] #获取sheet列表
#print(sheet_name)
api_sheet = api_file.sheet_by_name(sheet_name)
#print(api_sheet)
#读取所要绘制的接口名称
apiName = api_sheet.cell_value(1, 0)
#读取所要绘制图的excel文件
load_data=pd.DataFrame(pd.read_excel(api_results))
#获取需要展示的列名
load_plot=load_data['Durition(mms)']
#图表字体格式/字号
plt.rc('font', family='Microsoft YaHei', size=12)
#x = np.array([0,1,2])
#折线颜色/宽度/样式/透明度等
plt.plot(load_plot,color='#030303',linewidth=1,alpha=1)
#添加x轴标签
plt.xlabel("执行次数")
#设置x轴起始值
#plt.xlim(0,10)
#添加y轴标签
plt.ylabel('响应时间')
#设置y轴起始值
#plt.ylim(0,100)
#添加图表标题
plt.title(apiName)
#添加图表网格线，设置网格线颜色，线形，宽度和透明度
plt.grid( color='#95a5a6',linestyle='--', linewidth=1 ,axis='y',alpha=0.4)
#设置数据分类名称
#plt.xticks(x,('Data1','Data2','Data3'))
#输出图表
#plt.show()
#保存绘图到本地，不支持jpg
savefig("F:\\SlidePlus\\Result\\Picture\\Map_api_" + now_time + ".png")