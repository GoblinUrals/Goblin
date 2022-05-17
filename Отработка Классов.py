
class Ball:
    size=15
    def __init__(self,color,size=3):
        self.shape='Круглый'
        self.color=color
        self.size=size

    def __call__(self,param):
        return f"Я {param}{self.color}мяч"

    def __len__(self):
        a=[self.shape,self.color,self.size]
        return len(a)

    def jump(self,size):
        return self.size*size

    @classmethod
    def classmethod(cls):
        return cls.size

    @staticmethod
    def staticmethod():
        return 'Статика'
a=Ball('Воздушный')
print(Ball.staticmethod())
print(Ball.classmethod())
print(len(a))

#
# class Ball:
#     size = 15
#
#     def __init__(self, color, size=8):
#         self.shape = 'Круглый'
#         self.color = color
#         self.size = size
#
#     def __call__(self):
#         return f" Я {self.shape} мяч "
#
#     #def __len__(self):
#         #a=[self.shape,self.color,self.size]
#         #return len(a)
#         #return self.size*2
#
#     def __getitem__(self,key):
#         return [self.shape,self.color,self.size][key]
#
#     def jump(self, size):
#         return self.size * size
#
#     @classmethod
#     def classmethod(cls):
#         return cls.size
#
#     @staticmethod
#     def staticmethod():
#         return 'Статика'
# #a=Ball('Воздушный')
# #print(a[2])
# print(Ball('Воздушный')())
# print(Ball('1','2')())
#

