# class Parent:
#     def __init__(self):
#         self.attr_1 = 'I am parent'
#
#
#     def parent_method(self):
#         print('How are you?')
#
# #Создание класса_наследника
# class Child(Parent):
#     def __init__(self):
#         super().__init__(),
#         self.attr_2 = 'I am a child'
#
# #Создание ЭК Child
# chld = Child()
#
# #Атрибуты и методы Child
# print(chld.attr_2)
# print(chld.attr_1)
# chld.parent_method()

class Total:
    def __init__(self):
        #private attribute
        self._amount = None

    # Built-in @property decorator makes usage of
    # getter and setter easier .
    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, val):
        if val < 0:
            raise ValueError("Amount can't be lower than zero(0)")
        self._amount = val

v1 = Total()
v1.amount = 30
print(v1.amount)  # Output: 30

v2 = Total()
v2.amount = -5
# ValueError: Amount can't be lower than zero(0)