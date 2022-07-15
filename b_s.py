class Duck:

    def quack(self):
        print('Quack, quack')

    def fly(self):
        print('Flap, Flap!')

class Person:

    def quack(self):
        print("I'm Quacking Like a Duck!")

    def fly(self):
        print("I'm Flapping my Arms!")

def quack_and_fly(thing):
    try:
        thing.quack()
        thing.fly()
        thing.barc()
    except AttributeError as e:
        print (e)

    print()

d = Duck()

quack_and_fly(d)

p = Person()

quack_and_fly(p)







# d = Duck()
#
# print(type(dir(d)))