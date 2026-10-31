from car import Car

car1 = Car("Mustang",1969,"Silver",False)
car2= Car("Dodge",1969,"Black",True)
car3= Car("BMW",2020,"white",True)

print(car1.color)
print(car2.model)
print(car3.for_sale)
car2.drive()
car3.stop()