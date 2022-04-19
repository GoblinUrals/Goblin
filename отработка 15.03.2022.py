def func(num1):
    def number(num2):
        return num1*num2
    return number
a=func(6)(2)
print(a)


def func(a: int=1):
    def number(m):
        return m*2
    n={'1':number(a)+1,'2':number(a)+2}
    return(n)
m=func(5)
print(m,m['2'])

# создание генератора
def generator(n):
    for number in range(n):
        yield number+1
a=generator(5)
#print(a)
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))


import time

def delay(times):
    def decorator(func):

        def wrapper(*args):
            print('Выполняем функцию')
            time.sleep(times)
            result=func(args)
            print('Выполняем действия после')
            return result
        return wrapper
    return decorator
@delay(4)
def text(t):
    return t

print(text('123'))
