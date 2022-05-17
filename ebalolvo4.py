class Ball:
    size=15
    def __init__(self, color, size=3):
        self.shape = 'Круглый'
        self.color = color
        self.size = size

    def __call__(self,param):
        return print(f'Я{param} {self.color} мяч')

    def __len__(self):
        a=[self.size, self.color, self.size]
        return print(len(a))

    def jump(self,size):
        return print(self.size*size)

    @classmethod
    def classmethod(cls):
        return cls.size

    @staticmethod
    def staticmethod():
        return print('Статика')


print(Ball('Grey').size)
print(Ball('Grey').color)
Ball('Grey').__call__('Fat')
Ball('Grey').jump(size=15)
Ball('Grey').__len__()



ball=Ball('Grey')
ball.staticmethod()
print(ball.classmethod())
Ball('Grey')

