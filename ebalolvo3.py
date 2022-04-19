import threading
import time
import logging


logging.basicConfig(level=logging.DEBUG,
                    format='(%(threadName)-9s) %(message)s', )

def f():
    logging.debug('thread функция запущена')
    return



if __name__=='__main__':
    t1=threading.Timer(5, f)
    t1.setName('t1')
    t2=threading.Timer(5, f)
    t2.setName('t2')

    logging.debug('Стартует таймер....')
    t1.start()
    t2.start()

    logging.debug('Ожидание пока не завершиться %s',  t2.getName())
    time.sleep(2)
    logging.debug('Завершение %s',   t2.getName())
    print('Перед остановкой t2.is_alive() = ', t2.is_alive())
    t2.cancel()
    time.sleep(2)
    print('После остановки t2.is_alive() = ', t2.is_alive())

    t1.join()
    t2.join()
