f = open("config")
config = f.read().split("\n")[:-1]
host = config[0].split(" ")[1]
port = config[1].split(" ")[1]
user = config[2].split(" ")[1]
passwd = config[3].split(" ")[1]
db = config[4].split(" ")[1]
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
