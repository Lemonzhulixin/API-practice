import xlrd  #excel扩展库

filename = "F:\\SlidePlus\Result\\CreateExcel.xls"
file = xlrd.open_workbook(filename)
sheet_name = file.sheet_names()[0]
sheet = file.sheet_by_name(sheet_name)
#print(sheet_name)

count_rows = sheet.nrows  # 获取行数
count_cols = sheet.ncols  # 获取列数
print("Rows %d, Cols %d" % (count_rows, count_cols))

cell_value = sheet.cell_value(1,0) #获取第二行，第一列数据
print(cell_value)

#按行读取数据
for i in range(count_rows):
   data=sheet.row_values(i)
   print(data)


#读取sheet list
api_results = "F:\\SlidePlus\Result\\VivaVideo_api.xls" #单个接口所有运行结果写入的Excel文件名称
file = xlrd.open_workbook(filename)#打开VivaVideo_results.xls
#print(len(file.sheets()))
i = 0
while i < len(file.sheets()):
      sheet_name = file.sheet_names()[i] #遍历VivaVideo_results.xls中sheet名称
      print(sheet_name)
      try:
          sheet = file.sheet_by_name(sheet_name)
          i = i + 1
      except:
          print("No sheet in %s named %s" % (filename,sheet_name))
else:
   print("The end")





