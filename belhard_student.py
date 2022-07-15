class Vector:
    mini = 0
    maxi = 100

    @classmethod
    def validate(cls, arg):
        return cls.mini <= arg <= cls.maxi

print(Vector.validate(5))
v1 = Vector()
print(v1.validate(750))
print(v1.mini,v1.maxi)


class Vector:
    _mini = 120
    __maxi = 145

class Buki(Vector):
    def what_i_see(self):
        return self._mini

v1 = Vector()

print(v1._mini)
print(v1._Vector__maxi)