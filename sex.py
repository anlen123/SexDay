import pymysql
from pymysql.cursors import DictCursor
import random
conn = pymysql.connect(host="123.56.145.243", port=3307, user="root", passwd="123456", db="test", charset="utf8")
cur = conn.cursor(DictCursor)
import os
try:
    if os.path.exists("README.md"):
        os.system("rm -rf  README.md")
    with open("README.md", "a+")as f:
	f.write("# SexDay\n")

    for _ in range(20):
        sql = "select download_url from urls where id ={};".format(random.randint(1, 240000))
        cur.execute(sql)
        res = cur.fetchall()
        with open("README.md", "a+")as f:
            for x in res:
                # print(x['download_url'])
                f.write("![]({})\n".format(x['download_url']))
except:
    print("no")
finally:
    cur.close()
    conn.close()

