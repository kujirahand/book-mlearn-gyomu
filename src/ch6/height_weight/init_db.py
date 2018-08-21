import sqlite3

dbpath = "./hw.sqlite3"
sql = '''
  CREATE TABLE IF NOT EXISTS person (
      id INTEGER PRIMARY KEY,
      height NUMBER,
      weight NUMBER,
      typeNo INTEGER
  )
'''
with sqlite3.connect(dbpath) as conn:
    conn.execute(sql)
