

# class GameObject:
#     __x: int
#     __y: int

#     def __init__(self, x, y):
#         self.__x = x
#         self.__y = y

#     @property
#     def x(self):
#         return self.__x

#     @property
#     def y(self):
#         return self.__y

#     def move(self, delta_x, delta_y):
#         self.__x += delta_x
#         self.__y += delta_y

# GameObject().move(10,18)
# # print(game.move())


def reverse(s):
    str = ''
    for i in s:
        str += i
        return str

print(reverse('Python'), end='')