# from abc import ABC, abstractmethod
#
# class Basic(ABC):
#
#     @abstractmethod
#     def hello(self):
#         print('Привет от Basic')
#
#
# class Advanced(Basic):
#     def hello(self):
#         super().hello()
#         print('Вывели основной')
# a = Advanced()
# a.hello()
class Gameobject:
    __x: int
    __y: int

    def __init__(self,x,y):
        self.__x=x
        self.__y=y

    @property
    def x(self):
        return self.__x
    @property
    def y(self):
        return self.__y

    def move(self,delta_x,delta_y):
        self.__x+=delta_x
        self.__y+=delta_y
