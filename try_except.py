import random

def dangerous_code():
    value = random.randint(0,10)
    if value%2==0:
        raise ValueError ('четное значение')
    else:
        return value

try:
    some_value = 0
    try:
        some_value = dangerous_code()
    except ValueError as exc:
        print('возникло вложенное исключение')
    print(f'Результат: {some_value}')
except Exception as exc:
    print('возникло исключение')






