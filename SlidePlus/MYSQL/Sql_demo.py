import MySQLdb
import os

try:
    conn = MySQLdb.connect(host='localhost', port=3306, user='root', passwd='Zlx123456')
    cur = conn.cursor()

    cur.execute("DROP database IF EXISTS python")
    cur.execute('create database if not exists python')
    # conn.select_db('python')
    # cur.execute('create table test(id int,info varchar(20))')
    #
    # value = [1, 'hi Lemon']
    # cur.execute('insert into test values(%s,%s)', value)
    #
    # values = []
    # for i in range(10):
    #     values.append((i, 'hi Lemon' + str(i)))
    # cur.executemany('insert into test values(%s,%s)', values)
    # cur.execute('update test set info="I am Lemon" where id=3')
    # conn.commit()
    cur.close()
    conn.close()
except BaseException as e:
    print(e)
