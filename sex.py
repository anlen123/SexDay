f = open("config")
config = f.read().split("\n")[:-1]
print(config)
host = config[0]
port = config[1]
user = config[2]
passwd = config[3]
db = config[4]
print(host,port,user,passwd,db)
import pymysql
from pymysql.cursors import DictCursor
import random
conn = pymysql.connect(host=str(host), port=int(port), user=str(user), passwd=str(passwd), db=str(db), charset="utf8")
cur = conn.cursor(DictCursor)
import os
try:
    if os.path.exists("README.md"):
        os.system("rm -rf  README.md")
    with open("README.md", "a+")as f:
        f.write("# SexDay\n")

    for _ in range(100):
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

f.close()
