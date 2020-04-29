import os

file_format = [".json"]

class FileFilt:
    fileList = [ ]
    counter = 0
    def __init__(self):
        pass
    def FindFile(self, path, filtrate=1):
        global file_format
        for s in os.listdir(path):#返回指定目录下的所有文件和目录名
            newDir = os.path.join(path, s) #将多个路径组合后返回，第一个绝对路径之前的参数将被忽略；os.path.join('路径','文件名.txt')
            if os.path.isfile(newDir): #如果path是一个存在的文件，返回True。否则返回False。
                if filtrate:
                    if newDir and (os.path.splitext(newDir)[1] in file_format): #os.path.splitext():分离文件名与扩展名
                        self.fileList.append(newDir)
                        self.counter += 1
                else:
                    self.fileList.append(newDir)
                    self.counter += 1

if __name__ == "__main__":
    b = FileFilt()
    b.FindFile(path="F:\\SlidePlus\\Report")
    #print(b.fileList)
    for json_file in b.fileList:
        filename = os.path.basename(json_file)
        print(filename)
