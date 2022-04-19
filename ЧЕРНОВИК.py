# from abc import ABC, abstractmethod
#
# class Device(ABC):
#     name: str
#
#     @abstractmethod
#     def procecc_doc(self,name):
#         self.name=name
#
# class Scanner(Device):
#
#     def procecc_doc(self,name):
#         super().procecc_doc(name)
#         return print(f'Сканирую документ: {self.name}')
#
# class Copier(Device):
#
#     def procecc_doc(self,name):
#         super().procecc_doc(name)
#         return print(f'Делаю копию : {self.name}')
#
# class MFU(Scanner, Copier):
#
#     def procecc_doc(self,name):
#         super().procecc_doc(name)
#         return print(f'Сканирую и отправляю факс :{self.name}')
#
# a=MFU()
# a.procecc_doc('строка')
# print(MFU.mro())
from abc import ABC


class Animal(ABC):
    name: str

    def __init__(self, name):
        self.name = name

    def says(self):
        pass


class Cat(Animal):
    name: str

    def __init__(self, name):
        super().__init__(name)

    def says(self):
        return f"{self.name} - кошка. Говорит МЯУ!"


class Dog(Animal):
    name: str

    def __init__(self, name):
        super().__init__(name)

    def says(self):
        return f"{self.name} - собака. Говорит ГАВ!"


class Cow(Animal):
    name: str

    def __init__(self, name):
        super().__init__(name)

    def says(self):
        return f"{self.name} - корова. Говорит МУ!"

name='Маруся'
a=(Cat(name),Dog(name),Cow(name))
for tex in a:
    print(tex.says())