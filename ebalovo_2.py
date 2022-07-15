# class y:
#     a = 8
#     b = 98
#     def __ge__(self):
#         print("Inside ge Dunder")
# z = y()
# print((z.a).__ge__(z.b))
from os import remove

a = 'В последнем случае словарь эффективно заменяет условные конструкции if – elif – else. ' \
	'В качестве ключей в словарях можно использовать только неизменяемые типы данных – цифры, строки (включая «сырые»)' \
	' и кортежи. Однако в качестве значений можно использовать почти любые типы данных.'


z = a.strip('-').split()

q = sorted(z, key = lambda x: len(x))

b = list(filter(lambda x: x != "ключей", q))

print(b)




# a = [1,3,7,9,5,78,65,100,5,7]

# for i in a:
#     if a==5:
#         a.remove(5)
# print(a)
# # b = []
# for i in range(len(q)):
#     if  q[i] == 'if':
#         q.remove(q[i])

# print(q)

# a = [1,3,7,9,5,78,65,100,5,7]
# for i in range(len(a)):
#     if a[i]=='5':
#         a.pop(i)
# print(a)
