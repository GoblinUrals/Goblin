class SoftwareEngineer:
    def __init__(self, name):
        self.name = name



    def __repr__(self):
        return "%s.%s(name=%s)" % (self.__class__.__module__,
                                   self.__class__.__qualname__,
                                   self.name)

    def __str__(self):
        return "Software Engineer named %s" % (self.name)

se = SoftwareEngineer('Vlados')

print(se)
print(se.__str__())
print(str(se))

print(se.__repr__())
print(repr(se))

# class Finxter(object):

#     def __str__(object):
#         return str ('Fialka')
#
#     def __repr__(object):
#         return repr('Romashka')
#
# print(Finxter())
# print(Finxter().__str__())
# print(str(Finxter()))
#
# print(Finxter().__repr__())
# print(repr(Finxter()))
#
#
# print(eval(repr(Finxter())))
# print(eval(Finxter().__repr__()))


import math

class Vector2D:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return '{}, {}'.format(self.x, self.y)

    def __repr__(self):
        return 'Vector2D({}, {})'. format(self.x, self.y)

    def __add__(self, other):
        return Vector2D(self.x + other.x, self.y + other.y)

    def __iadd__(self, other):
        self.x+=other.x
        self.y+=other.y
        return self

    def __sub__(self, other):
        return Vector2D(self.x - other.x, self.y - other.y)

    def __isub__(self, other):
        self.x-=other.x
        self.y-=other.y
        return self

    def __abs__(self):
        return math.hypot(self.x, self.y)

    def __bool__(self):
        return self.x!=0 or self.y!=0

    def __neg__(self):
        return Vector2D(-self.x, -self.y)

x = Vector2D(3,4)
y = Vector2D(5,6)

print(x.__repr__())
print(x.__str__())
print(x.__abs__())
print(x.__bool__())
print(x.__neg__())
print(x.__add__(x))
print(x.__iadd__(y))
print(x.__isub__(y))
