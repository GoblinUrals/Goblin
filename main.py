# import threading
# import time
#
# time1=time.time()
#
# def count(num: int):
#     return print(num*2)
#
# for n in range(1,5):
#     count(n)
# print(time.time()-time1)
#
#
#
# import threading
# import time
#
# time1=time.time()
#
# def count(num: int):
#     return print(num*2)
#
# for n in range(1,5):
#     thread=threading.Thread(target=count, args=(n, ))
#     thread.start()
#
# print(time.time()-time1)

# import multiprocessing
# import time
#
# t1=time.time()
#
# def worker(num):
#     return print(num*2)
#
# if __name__=='__main__':
#     jobs=[]
#     for i in range(1,5):
#         p=multiprocessing.Process(target=worker, args=(i,))
#         jobs.append(p)
#         p.start()
#
# print(t1-time.time())

# import logging
# logging.basicConfig(filename='example.log', encoding='utf-8', level=logging.DEBUG)
# logging.debug('This message should go to the log file')
# logging.info('So should this')
# logging.warning('And this,too')
# logging.error('And non-ASCII stuff, too, like resund and malmo')
