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
#删除已存在的表格
cur.execute('DROP TABLE IF EXISTS MAP_API')
#创建表格
cur.execute('CREATE TABLE MAP_API(api varchar(50),url varchar(50),method varchar(50),durition int,code int,status varchar(50))')
#查询要展示的接口信息
cur.execute('SELECT * FROM results where api = "ad-用户退出"')
#使用fetchall函数，将结果集（多维元组）存入rows里面
rows = cur.fetchall()
#依次遍历结果集，发现每个元素，就是表中的一条记录，用一个元组来显示
for row in rows:
    #print(row)
    cur.execute('INSERT INTO MAP_API VALUES(%s,%s,%s,%s,%s,%s)',row)
conn.commit()
cur.close()

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
title = pd.read_sql_query('SELECT api FROM map_api LIMIT 1', conn)
print(title)
plt.title(title)
#添加图表网格线，设置网格线颜色，线形，宽度和透明度
plt.grid( color='#95a5a6',linestyle='--', linewidth=1 ,axis='y',alpha=0.4)
#设置数据分类名称
#plt.xticks(x,('Data1','Data2','Data3'))
#输出图表
#plt.show()
#保存绘图到本地，不支持jpg
savefig("F:\\SlidePlus\\Result\\Picture\\Map_api_" + now_time + ".png")

conn.close() #关闭数据库连接