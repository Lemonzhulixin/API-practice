# -*- coding: UTF-8 -*-
import MySQLdb
import time
#导入绘图库
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.pyplot import savefig
import seaborn as sns

conn = MySQLdb.connect(host='localhost', port=3306, user='root', passwd='Zlx123456',database='vivavideo', charset='utf8')
cur = conn.cursor()
now_time = time.strftime("%Y%m%d%H%M%S", time.localtime(time.time()))
data1 = pd.read_sql_query('SELECT durition FROM results where api = "ad-用户退出"',conn)
data2 = pd.read_sql_query('SELECT durition FROM results where api = "dg-设备登录-iOS"',conn)

sns.distplot(data1,kde=False,rug=True)
plt.show()

cur.close()
conn.close()