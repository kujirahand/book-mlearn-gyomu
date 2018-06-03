import sqlite3
import random

dbpath = "./hw.sqlite3"

def insert_db(conn):
    # ダミーで身長と体重と体型データを作る --- (*1)
    height = random.randint(130, 180)
    weight = random.randint(30, 100)
    # 体型データはBMIに基づいて自動生成 --- (*2)
    type_no = 1
    bmi = weight / (height / 100) ** 2
    if bmi < 18.5:
        type_no = 0
    elif bmi < 25:
        type_no = 1
    elif bmi < 30:
        type_no = 2
    elif bmi < 35:
        type_no = 3
    elif bmi < 40:
        type_no = 4
    else:
        type_no = 5
    # SQLと値を指定してDBに値を挿入 --- (*3)
    sql = '''
      INSERT INTO person (height, weight, typeNo) 
      VALUES (?,?,?)
    '''
    values = (height,weight, type_no)
    print(values)
    conn.executemany(sql,[values])

# DBに接続して100件のデータを挿入
with sqlite3.connect(dbpath) as conn:
    # データを100件挿入 --- (*4)
    for i in range(100):
        insert_db(conn)
    # トータルで挿入した行数を調べる --- (*5)
    c = conn.execute('SELECT count(*) FROM person')
    cnt = c.fetchone()
    print(cnt[0])
