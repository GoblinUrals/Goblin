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

