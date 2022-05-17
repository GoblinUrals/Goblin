class Transport:
    brand:str
    model:str
    color:str

    def __init__(self,brand,model,color):
        self.brand=brand
        self.model=model
        self.color=color

    def move(self,distance):
        print(f'{self.brand}{self.model}может двигаться')

class Car(Transport):
    vin: str
    issue_year:str
    mileage:int

    def __init__(self,brand,model,color,vin,issue_year,mileage=0):
        super().__init__(brand,model,color)
        self.vin=vin
        self.issue_year=issue_year
        self.mileage=mileage

    def move(self,distance):
        print(f'{self.model}вжжжжк')
        self.mileage+=distance

    def signal(self):
        print(f'{self.supra} бип-бип')

supra=Car(
    'Toyota',
    'Supra a80',
    'black',
    'JT4RN13P7K0001611',
    1995,
    215000
)


import math

class Vector2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return 'Vector2D({}, {})'.format(self.x, self.y)

    def __str__(self):
        return '({}, {})'.format(self.x, self.y)

    def __add__(self, other):
        return Vector2D(self.x + other.x, self.y + other.y)

    def __iadd__(self, other):
        self.x += other.x
        self.y += other.y
        return self

    def __sub__(self, other):
        return Vector2D(self.x - other.x, self.y - other.y)

    def __isub__(self, other):
        self.x -= other.x
        self.y -= other.y
        return self

    def __abs__(self):
        return math.hypot(self.x, self.y)

    def __bool__(self):
        return self.x != 0 or self.y != 0

    def __neg__(self):
        return Vector2D(-self.x, -self.y)






























































#class Human:
    #def __init__(self,height,weight,age):
        #self.height=height
        #self.weight=weight
        #print(self.height)
        #self.age=age

    #def hair(self):
        #return 'шатен'

#class Boy(Human):
    #def __init__(self,height,weight,age,sex,hair):
        #super().__init__(height,weight,age)
        #self.sex=sex
        #self.hair=hair

    #def old (self):
        #return self.age+1

#print(Boy(120,80,13,'m','темный').old())
#class Girl(Human):

    #def __init__(self,height,weight,age,sex,hair):
        #super().__init__(height,weight,age)
        #self.sex=sex
        #self.hair=hair

    #    return self.age+1

#print(Boy(120,80,13,'m','темный').old())
#print(Girl(110,60,12,'w','светлый').old())



#class Vanya:
      #def __init__(self):
        #self.param=Petya()

#print(Vanya().param.sex)
#print(Petya().sex)

#print(Petya().sex)

