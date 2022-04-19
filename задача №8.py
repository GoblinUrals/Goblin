# from datetime import date
# CURRENT_YEAR=date.today().year
#
# class BookCard:
#     __author: str
#     __title: str
#     __year: int
#
#     def __init__(self,__author,__title,__year):
#         self.__author=__author
#         self.__title=__title
#         self.__year=__year
#
#     def sorting_book(self):
#         pass
#
#     @property
#     def get_author(self):
#         return self.__author
#
#     @get_author.setter
#     def get_author(self,new_author):
#         if isinstance(new_author,str):
#             self.__author=new_author
#         else:
#             raise ValueError('Не верное значение')
#
#     @property
#     def get_title(self):
#         return self.__title
#
#     @get_title.setter
#     def get_title(self,new_title):
#         if isinstance(new_title,str):
#             self.__title=new_title
#         else:
#             raise ValueError('не верное значение')
#
#     @property
#     def get_year(self):
#         return self.__year
#
#     @get_year.setter
#     def get_year(self,new_year):
#         if isinstance(self.__year,int):
#             if 0<new_year<=CURRENT_YEAR:
#                 self.__year=new_year
#             elif new_year <=0:
#                 raise ValueError ('')
#             else:
#                 raise ValueError ('')
# #
# from abc import ABC, abstractmethod
#
# class Transport(ABC):
#     brand: str
#     model: str
#     issue_year: int
#     color: str
#     mileage: int
#
#     def __init__(self, brand, model,issue_year, color):
#         self.mileage=0
#         self.brand = brand
#         self.model = model
#         self.issue_year=issue_year
#         self.color = color
#
#     @abstractmethod
#     def move(self,mileage,num:int):
#         self.mileage = mileage
#         self.num=num
#         if self.num>0:
#             self.num=self.mileage+self.num
#         else:
#             raise ValueError ('Расстояние должно быть положительным числом')
#
# class Car(Transport):
#     engine_type: str
#
#     def __init__(self,brand,model,issue_year,color,engine_type):
#         super().__init__(brand,model,issue_year,color)
#         self.engine_type=engine_type
#
#     def move(self,mileage,num):
#         super().move(mileage,num)
#         return (f'{self.brand}{self.model} ({self.color}-{self.issue_year}) проехала {self.num} км')
#
# class Airplane(Transport):
#     lifting_capacity: int
#
#     def __init__(self,brand,model,issue_year,color,lifting_capacity):
#         super().__init__(brand, model, issue_year, color)
#         self.lifting_capacity=lifting_capacity
# #
#     def move(self,mileage,num):
#         super().move(mileage,num)
#         return (f'{self.brand}{self.model} ({self.color}-{self.issue_year}) пролетела  {self.num} км')

