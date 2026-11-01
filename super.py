class Shape:
    def __init__(self,color,is_filled):
        self.color = color
        self.is_filled = is_filled
    def describe(self):
        print(f"The color is {self.color} and area is filled {self.is_filled}")

class Square(Shape):
    def __init__(self,color,is_filled,length,width):
        super().__init__(color, is_filled)
        self.width = width
        self.length = length
    
    def describe(self):
        print(f"The area of the square is {self.length * self.width}")
        super().describe() 

class Circle(Shape):
    def __init__(self,is_filled,color,radius):
        super().__init__(color,is_filled)
        self.radius = radius
    
        super().describe() ## method override from super class if method not defined.
    def describe(self): #3 method defined
        print(f"The radius of the circle is {self.radius * 2}")
        

square = Square("Red",True,10,20)
circle = Circle(color = "Yellow",is_filled = False,radius=100) ##different type of declaration
circle1 = Circle("Green",True,30)

print(circle1.color)
print(square.color)
square.describe() ## Super class override
print(circle.color)
circle.describe()  ## Super class override

