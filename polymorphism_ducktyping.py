class Animal:
    Alive = True

class Cat(Animal):
    def speak(self):
        print("MEOW!!")

class Dog(Animal):
    def speak(self):
        print("WOOF")

class Car():                   ## Ducktyping polymorphism because of of animal class present and method is used.
    Alive = False              ## Accessible  - Named same as other inherited classes hence ducktyping
    def speak(self):           ## Method - Named same as other inherited classes hence ducktyping
        print("WROOM")

speak = [Cat(),Dog(),Car()]

for speak in speak:
    speak.speak()
    print(speak.Alive)  