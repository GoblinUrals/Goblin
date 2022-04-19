class Human:
    def __init__(self,height,weight,age):
        self.height=height
        self.weight=weight
        self.age=age
        self.sex=None

    def hair(self):
        return 'шатен'

class Boy(Human):
    def __init__(self,height,weight,age,hair):
        super().__init__(height,weight,age)
        self.sex='m'
        self.hair=hair

    def old (self):
        return self.age+1

class Petya(Boy):
    def __init__(self):
        height=120
        weight=50
        age=12
        hair='темный'
        super().__init__(height,weight,age,hair)

class Girl(Human):

    def __init__(self,height,weight,age,sex,hair):
        super().__init__(height,weight,age)
        self.sex=sex
        self.hair=hair

    def old(self):
        return self.age+1


class Vanya:
      def __init__(self):
        self.param=Petya()

print(Vanya().param.sex)
print(Petya().sex)


