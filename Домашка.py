# while True:
#     try:
#         a = float(input('Введите первое число: '))
#         s = input('Знак(+,-,*,/):')
#         b = float(input('Введите второе число: '))
#         if s == '+':
#             print('Итог:', (a + b))
#         elif s == '-':
#             print('Итог:', (a - b))
#         elif s == '/':
#             print('Итог:', (a / b))
#         elif s == '*':
#             print('Итог:', (a * b))
#     except ZeroDivisionError:
#         print('Ошибка.Деление на 0')
#     except ValueError:
#         print('Вводим только цифры!')
#     c=input('Желаете продолжить ? (y,n) :')
#     if c=='y':
#         continue
#     else:
#         break


class GameObject:
    __x: int
    __y: int

    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    def move(self, delta_x, delta_y):
        self.__x += delta_x
        self.__y += delta_y

GameObject().move(10,18)
# print(game.move())