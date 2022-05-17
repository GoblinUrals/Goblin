class Ball:
    size=15
    def __init__(self, color, size):
        self.shape = 'Круглый'
        self.color = color
        self.size = size

    def __call__(self):
        return print(f'Я {self.shape} мяч')

    def __len__(self):
        a=[self.size, self.color, self.size]
        return (len(a))

    def jump(self,size):
        return print(self.size*size)

    @classmethod
    def classmethod(cls):
        return cls.size

    @staticmethod
    def staticmethod():
        return ('Статика')

ball=Ball('Grey',11)

print(ball())
print(Ball('Grey',11).__call__())
print(f'{ball.color}\n'  f'{ball.size}\n')
