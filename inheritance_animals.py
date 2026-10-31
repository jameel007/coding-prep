class Animal:
    def __init__(self,name):
        self.name = name
        self.is_alive = True

    def eat(self):
        print(f"{self.name} is eating")

    def sleep(self):
        print(f"{self.name} is sleeping")

class Dog(Animal):   ## Inheritance
    def speak(self):
        print("Woof!")

class Cat(Animal):
    def speak(self):
        print("Meow!")

dog = Dog("Scooby") 
cat = Cat("Minnu")

print(dog.is_alive)
cat.is_alive
print(dog.eat())
print(dog.speak())
print(cat.sleep())
print(cat.speak())