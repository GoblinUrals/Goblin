# import sqlite3
#
# conn=sqlite3.connect('databases.db')
# cur=conn.cursor()
#
# #cur.execute("CREATE TABLE users (id SERIAL, first_name text,second_name text);")
#
# def insert(first_name,second_name):
#     cur.execute(f" INSERT INTO users (first_name, second_name) VALUES ('{first_name}', '{second_name}')")
#     conn.commit()
#
#


import threading
import time

time1=time.time()
def count(num: int):
    return  print(num*2)

for n in range(1,9):
    thread=threading.Thread(target=count, args=(n, ))
    thread.start()
print(time.time()-time1)
