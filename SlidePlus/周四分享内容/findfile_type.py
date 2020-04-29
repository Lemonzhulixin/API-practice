import os

file_format = [".json"] #需要查询的文件类型
fileList = [ ]
name = [ ]
counter = 0
path = "F:\\SlidePlus\\Report"  #自动化报告json文件路径
json_results = "F:\\SlidePlus\Result\\VivaVideo_results.xls" #所有接口运行结果写入的Excel文件名称

for files in os.listdir(path):#返回指定目录下的所有文件和目录名
    if files and (os.path.splitext(files)[1] in file_format):  # os.path.splitext():分离文件名与扩展名 files带有文件路径和后缀，[1]是数组后缀
       fileList.append(files)
       counter += 1
print(fileList)

for file in fileList:
    print(file)

#仅获取文件名，无后缀
#i = 0
#while i < len(fileList):
 #   sheet_name = os.path.splitext(fileList[i])[0] #注意[0]的位置
 #   print(sheet_name)
  #  i+=1
#else:
 #   print("XX")