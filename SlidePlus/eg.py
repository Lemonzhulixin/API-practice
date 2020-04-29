import xlwt  #导入excel库
import xlrd  #导入Excel的扩展工具库
#import Results_VivaVideo  #如果想一次性执行生成绘图，可以导入该文件
#导入绘图库
import pandas as pd
import matplotlib.pyplot as plt

json_results = "F:\\SlidePlus\Result\\VivaVideo_signal.xls" #所有接口运行结果写入的Excel文件名称
test_results = "F:\\SlidePlus\Result\\Map_VivaVideo_result.xls" #所有运行结果计数写入的Excel文件名称
file = xlrd.open_workbook(json_results)#打开VivaVideo_results.xls
result_wb = xlwt.Workbook()  # 创建新的excel文件
result_ws = result_wb.add_sheet("Test Result")  # 创建sheet
# 新sheet的表格列值
result_ws.write(0, 0, "Status")
result_ws.write(0, 1, "Count")

# 获取所要展示的接口对应数据
sheet_name = file.sheet_names()[0] #获取VivaVideo_signal.xls中sheet名称
sheet = file.sheet_by_name(sheet_name)

count_rows = sheet.nrows   # 获取行数
count_cols = sheet.ncols  # 获取列数
length = count_cols/7
failed = 0
passed = 0
i = 0
while i < length:
    a = 1
    while a < count_rows:
        cell_value = sheet.cell_value(a, 7 * i + 5)  # 获取test result 列值
        # print(cell_value)
        if cell_value != "OK":  # 如果测试结果不等于OK，failed加1并跳过当前sheet
            failed = failed + 1
            # print(sheet_name,a,cell_value)
            break
        a = a + 1
    else:
        passed = passed + 1  # 如果测试结果都是OK，passed加1
        a = a + 1
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