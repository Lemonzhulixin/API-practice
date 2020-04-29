import xlrd  #导入Excel的扩展工具库
#导入绘图库
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

api_results = "F:\\SlidePlus\Result\\Map_VivaVideo_api.xls" #单个接口所有运行结果写入的Excel文件名称
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
plt.show()