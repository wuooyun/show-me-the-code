#!/usr/bin/env python3
import random
import string
import sqlite3

###----生成激活码
def random_char(y):
       return ''.join(random.choice(string.ascii_letters) for x in range(y))


def gen_keys(x,len=8):
    for _ in range(x):
        yield random_char(8)
    
###----存入数据库
conn = sqlite3.connect('app.db')
c = conn.cursor()

try:
    c.execute('''CREATE TABLE IF NOT EXISTS active_keys
                (key text,actived INTEGER)''')
except:
    print ("Create table failed")
    

for k in gen_keys(200):
    c.execute("INSERT INTO active_keys(key,actived) VALUES (?,?)",(k,0))

for row in c.execute("SELECT * FROM active_keys"):
    print (row) 

conn.commit()

c.close()