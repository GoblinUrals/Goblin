import threading
import time
import logging


logging.basicConfig(level=logging.DEBUG,
                    format='(%(threadName)-9s) %(message)s', )

def consumer(cv):
    logging.debug('Потребитель начал работу....')
    with cv:
        logging.debug('Потребитель ожидает...')
        cv.wait()
        logging.debug('Потребитель потребляет запрос')

def producer(cv):
    logging.debug('Производитель начал работу...')
    with cv:
        logging.debug('Производитель готов к работе')
        logging.debug('Уведомляем всех потребителей')
        cv.notifyAll()


if __name__ == '__main__':
    condition=threading.Condition()
    cs1=threading.Thread(name='потребитель1', target=consumer, args=(condition,))
    cs2=threading.Thread(name='потребитель2', target=consumer, args=(condition,))
    pd=threading.Thread(name='производитель', target=producer, args=(condition,))

    cs1.start()
    time.sleep(2)
    cs2.start()
    time.sleep(2)
    pd.start()

