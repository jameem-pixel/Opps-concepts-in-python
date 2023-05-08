# operator overloaded
class Vehicle:
    def __init__(self, fare):
        self.fare = fare
    def __add__(self, other):
        return self.fare+ other.fare
bus= Vehicle(20)
car= Vehicle(30)
total_fare=bus+ car
print(total_fare)

#Method Overloading
class Area:
    def find_area(self, a=None, b=None):
        if a != None and b != None:
            print("Rectangle:", (a * b))
        elif a != None:
            print("square:", (a * a))
        else:
            print("No figure assigned")
obj1=Area()
obj1.find_area()
obj1.find_area(10)
obj1.find_area(10,20)