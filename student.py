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
#
# with open(r'C:/Users/Влад/Desktop/students.txt') as file:
#     names=file.readlines()
#     for name in names:
#         _name=name.strip().split(' ')
#         first_name=_name[0]
#         second_name=_name[1]
#         insert(first_name,second_name)
#         print(first_name)


import threading
import time

time1=time.time()
def count(num: int):
    return  print(num*2)

for n in range(1,9):
    thread=threading.Thread(target=count, args=(n, ))
    thread.start()
print(time.time()-time1)
