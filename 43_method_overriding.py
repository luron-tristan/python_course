class Animal:
    def eat(self):
        print("This animal is eating")


class Rabbit(Animal):
    def eat(self):
        print("This rabbit is devouring a carrot")


rabbit = Rabbit()
rabbit.eat()
