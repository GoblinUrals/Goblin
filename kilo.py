
#
# from abc import ABC, abstractmethod
# class Basic():
#     __hiden: str
#
#     @property
#     def fun(self):
#         return self.__hiden
#
#     @fun.setter
#     def fun(self,val):
#         self.__hiden=val
#
#     def __init__(self,val):
#         self.__hiden=val+25
#
# a=Basic(2)
# print(a.fun)
# from abc import ABC, abstractmethod
#
# class Animal(ABC):
#     name: str
#     def __init__(self, name):
#         self.name = name
#
#     @abstractmethod
#     def says(self):
#         return ('ok')
#
# class Cat(Animal):
#     def says(self):
#         super().says()
#         return (f'{self.name} - кошка. Говорит МЯУ!')
#
# class Dog(Animal):
#     def says(self):
#         super().says()
#         return(f'{self.name} - собака. Говорит ГАВ!')
#
# class Cow(Animal):
#     def says(self):
#         super().says()
#         return(f'{self.name} - корова. Говорит МУ!')
#
#
# name='маруся'
# a=(Cat(name),Dog(name),Cow(name))
#
# for tex in a:
#     print(tex.says())
class Person:
    def __init__(self, fullname, phone):
        self.fullname = fullname
        self.phone = phone


class LibraryReader(Person):
    uid: int
    books: set

    def __init__(self, fullname, phone, uid, books=None):
        super().__init__(fullname, phone)
        if books is None:
            books = set()
        self.uid = uid
        self.books = books

    def take_books(self, *args):
        self.books = self.books.union(args)
        if len(args) <= 3:
            args = list(args)
            args.sort()
            return f"{self.fullname} взял(а) книги: {', '.join(args)}"
        else:
            return f'{self.fullname} взял(а) {len(args)} книги'

    def return_book(self, *args):
        args = set(args)
        if self.books.issuperset(args):
            self.books = self.books.difference(args)
            if len(args) <= 3:
                lst = list(args)
                lst.sort()
                return f"{self.fullname} вернул(а) книги: {', '.join(lst)}"
            else:
                return f'{self.fullname} вернул(а) {len(args)} книги'
        else:
            raise ValueError(f'{self.fullname} не брал(а): {args.difference(self.books)}')

x=LibraryReader('Струков',80296096761,('108145')).take_books('Струков', 80296096761, ('108145'), ('Дюма', 'Три', 'Мушкетера'))
print(x)