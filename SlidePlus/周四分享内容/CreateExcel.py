import xlwt


wb = xlwt.Workbook()  # 创建excel文件
ws = wb.add_sheet("CreateSheet")  # 创建sheet
# 表格列值
ws.write(0, 0, "姓名")
ws.write(0, 1, "性别")
ws.write(0, 2, "年龄")

#写入数据
ws.write(1, 0, "张三")
ws.write(1, 1, "男")
ws.write(1, 2, "18")

ws.write(2, 0, "李四")
ws.write(2, 1, "女")
ws.write(2, 2, "20")
#保存Excel文件
wb.save("F:\\SlidePlus\Result\\CreateExcel.xls")


