class Animal:
    def __init__(self,name):
        self.name = name
        
    def eat(self):
            print(f"This {self.name} is eating")
    def sleep(self):
        print(f"This {self.name} is sleeping")

class Prey(Animal):
    def flee(self):
        print("This is fleeing...")

class Predator(Animal):
    def hunt(self):
        print("This is Hunting!!!!!")

class Rabbit(Prey):
    pass

class Hawk(Predator):
    pass

class Fish(Prey,Predator):
    pass

rabbit = Rabbit("Bugs Bunny")
fish = Fish("Nemo")
hawk = Hawk("Khabib")

print(fish.flee())
print(fish.hunt())
print(hawk.hunt())

print(fish.eat())
print(fish.sleep())

rabbit.eat()  ## multiple inheritance of class and its attributes
rabbit.sleep()

