
# with open(r'C:/Users/Влад/Desktop/students.txt') as  file:
#     for num, string in enumerate(file.readlines()):
#         print(str(num) + ". " + string.strip())
#


# import re
#
# def func(filename, regex):
#     with open(filename) as f:
#         for line in f:
#             if re.search(regex, line):
#                 yield line.rstrip()
#
# for line in func('C:/Users/Влад/Desktop/students.txt', 'Струков '):
#     print(line)

with open(r'C:/Users/Влад/Desktop/students.txt') as  file:
    names = file.readlines()
    for name in names :
        _name= name.strip().split(' ')
        print(_name)
        first_name = _name[0]
        second_name = _name[1]
        print(first_name, second_name)
