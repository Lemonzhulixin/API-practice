conn = MySQLdb.connect(host='localhost', port=3306, user='root', passwd='Zlx123456')
cur = conn.cursor()

cur.execute('DROP database IF EXISTS vivavideo')
cur.execute('create database if not exists vivavideo')
conn.select_db('vivavideo')
cur.execute('create table results(api varchar(50),url varchar(50),method varchar(50),durition int,code int,status varchar(20))')
value1 = ['da','{{VivaVideoUrl_hz_d}}/da','post',100,200,'OK']
value2 = ['dg','{{VivaVideoUrl_hz_d}}/dg','post',88,500,'OK']
cur.execute('insert into results values(%s,%s,%s,%s,%s,%s)', value1)
cur.execute('insert into results values(%s,%s,%s,%s,%s,%s)', value2)
cur.execute('update results set method="get" where api ="da"')

conn.commit()
cur.close()
conn.close()