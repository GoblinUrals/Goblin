# c=[]
# for num in range(1,15):
#     c.append(num*2)
# print(c)
# print(f"{'hello':*<20}")
# print(f'{12458:*=10}')
# print('Hello world'.count('wo'))
# print('Hello world'.partition('l'))
# print('Hello world'.rpartition('ol'))
# print('Hello world'.rpartition('l'))
# a='я так думаю'
# print(f'f-строка {a} интересная тема')
#
# w='Струков Владислав Владимирович'
# print('sd_afx_xccs_jcoakc'.split('_'))
# print('43,543,765,3,765,432'.split(','))
# print(w.split('к'))
# w='Струков Владислав Владимирович'
# print(','.join(w.split()))
# q=['Струков', 'Владислав', 'Владимирович']
# print('='.join(q))
# z=['12','49','78','879','7456']
# #print(','.join(z.split()))
# print(' '.join(z))
#from sqlalchemy import types as sqltypes
#number=[1,2,3]
#print(dir(number))
# def some_function(name):
#     print(f'Hi{name}')
# if __name__=="__main__":
#     name=input('Put your name:')
#     some_function(name)

class Person:
    fullname: str
    phone: str

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


LibraryReader('Струков', 80296096761, 108145, ('Дюма', 'Три', 'Мушкетера')).take_books()