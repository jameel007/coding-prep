## Polymorphism is to have many forms.

from abc import ABC,abstractmethod
class Shape:
    
    @abstractmethod   ## Polymorphism cn be achieved through inheritance and ducktyping
    def area(self):
        pass

class Square:
    def __init__(self,side):
        self.side = side
    def area(self):
        return self.side**2


class Circle:
    def __init__(self,radius):
        self.radius = radius
    def area(self):
        return 3.14* self.radius**2

class Triangle:
    def __init__(self,base,height):
        self.base = base
        self.height = height

    def area(self):
        return self.base *self.height* 0.5

class Pizza(Circle):  ## Polymorphims - as takes properties of another form of property of inherited method of shape class in circle class
    def __init__(self,topping,radius):
        super().__init__(radius)
        self.topping = topping
    
    def area(self):
        return self.radius**2

shapes = [Circle(10),Square(30),Triangle(20,30),Pizza("Olives",30)]

for shape in shapes:
    print(f"The area of shapes are {shape.area()} cm²")

