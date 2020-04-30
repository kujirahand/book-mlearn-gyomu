import sqlite3

dbpath = "./hw.sqlite3"
select_sql = "SELECT * FROM person"

with sqlite3.connect(dbpath) as conn:
    for row in conn.execute(select_sql):
        print(row)

