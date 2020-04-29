# -*- coding: UTF-8 -*-
import MySQLdb
import time
#导入绘图库
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.pyplot import savefig

#连接mysql，获取连接的对象
conn = MySQLdb.connect(host='localhost', port=3306, user='root', passwd='Zlx123456',database='vivavideo', charset='utf8') #连接数据库
#获取连接的cursor对象，用于执行查询
cur = conn.cursor()
now_time = time.strftime("%Y%m%d%H%M%S", time.localtime(time.time()))  # 获取当前时间
#Read SQL query into a DataFrame.
load_data=pd.DataFrame(pd.read_sql_query('SELECT durition FROM results where api = "ad-用户退出"',conn))
#获取需要展示的列名
load_plot=load_data["durition"]
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
#title = pd.read_sql_query('SELECT api FROM map_api LIMIT 1', conn)
#print(title)
plt.title("ad-用户退出")
#添加图表网格线，设置网格线颜色，线形，宽度和透明度
plt.grid( color='#95a5a6',linestyle='--', linewidth=1 ,axis='y',alpha=0.4)
#设置数据分类名称
#plt.xticks(x,('Data1','Data2','Data3'))
#输出图表
#plt.show()
#保存绘图到本地，不支持jpg
savefig("F:\\SlidePlus\\Result\\Picture\\Map_api_" + now_time + ".png")

cur.close()
conn.close() #关闭数据库连接