import xlwt  #导入excel库
import xlrd  #导入Excel的扩展工具库
#import Results_VivaVideo  #如果想一次性执行生成绘图，可以导入该库
#导入绘图库
import pandas as pd
import matplotlib.pyplot as plt

json_results = "F:\\SlidePlus\Result\\VivaVideo_results.xls" #所有接口运行结果写入的Excel文件名称
test_results = "F:\\SlidePlus\Result\\Map_VivaVideo_result.xls" #所有运行结果计数写入的Excel文件名称
file = xlrd.open_workbook(json_results)#打开VivaVideo_results.xls
result_wb = xlwt.Workbook()  # 创建新的excel文件
result_ws = result_wb.add_sheet("Test Result")  # 创建sheet
# 新sheet的表格列值
result_ws.write(0, 0, "Status")
result_ws.write(0, 1, "Count")

# 获取所要展示的接口对应数据
i = 0
failed = 0
passed = 0
#result_list = []
while i < len(file.sheets()):
      sheet_name = file.sheet_names()[i] #遍历VivaVideo_results.xls中sheet名称
      try:
          sheet = file.sheet_by_name(sheet_name)
      except:
          print("No sheet in %s named %s" % (json_results,sheet_name))

      #count_cols = sheet.ncols  # 获取列数
      count_rows = sheet.nrows  # 获取行数
      a = 1
      while a < count_rows:
            cell_value = sheet.cell_value(a, 5) #获取test result 列值
            # print(cell_value)
            if cell_value != "OK": #如果测试结果不等于OK，failed加1并跳过当前sheet
                  failed = failed + 1
                  #print(sheet_name,a,cell_value)
                  break
            a = a + 1
      else:
            passed = passed + 1 #如果测试结果都是OK，passed加1
            a = a +1
      i = i + 1

else:
      print("The end")
#print("Passed:",passed)
#print("Failed:",failed)
result_ws.write(1, 0, "Passed" )
result_ws.write(1, 1, passed)
result_ws.write(2, 0, "Failed" )
result_ws.write(2, 1, failed)

result_wb.save(test_results) #保存Excel

#读取所要绘制图的excel文件
load_data=pd.DataFrame(pd.read_excel(test_results))

#图表字体为华文细黑，字号为15
plt.rc('font', family='Microsoft YaHei', size=10)
#设置画布大小
plt.figure(figsize=(6, 5.5))
#设置饼图中每个数据分类的颜色
colors = ["#00FF00","#EE0000"]
#设置饼图中每个数据分类的名称
name=['Passed', 'Failed']
load_data_grade = load_data['Count']
#创建饼图，设置分类标签，颜色和图表起始位置等
plt.pie(load_data_grade,labels=name,colors=colors,explode=(0, 0.05,),startangle=30,autopct='%1.1f%%')
#添加图表标题
plt.title('某天测试结果Passed与Failed占比')
#添加图例，并设置显示位置
plt.legend(['Passed','Failed'], loc='upper left')
#显示图表
plt.show()




