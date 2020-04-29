import xlwt  # 导入excel库
import xlrd  #excel扩展库
from xlutils.copy import copy #excel 扩展库

oldWb = xlrd.open_workbook("F:\\SlidePlus\Result\\CreateExcel.xls", formatting_info=True)
newWb = copy(oldWb)
newWs = newWb.add_sheet("NewSheet")
newWb.save("F:\\SlidePlus\Result\\CreateExcel.xls")




