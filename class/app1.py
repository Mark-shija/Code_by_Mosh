"""class inheritance"""


class Animal:
    def eat(self):
        print("Eat Food Now")


class Mammal(Animal):
    def walk(self):
        print("Walk by Running quickly")


class Fish(Animal):
    def Swim(self):
        print("Swim Now")


m = Mammal()
m.eat()

f = Fish()
f.Swim()

print(m)
print(f)
