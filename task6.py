import math

class Shape:
    def area(self):
        pass

class Square(Shape):
    def __init__(self,side):
        self.side = side

    def area(self):
        return self.side * self.side

class triangle(Shape):
    def __init__(self,base,height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius * self.radius

while True:
    print()
    print("Select an option:")
    print("1. Calculate the area of a square")
    print("2. Calculate the area of a triangle")
    print("3. Calculate the area of a circle")
    print("4. Exit")
    
    
    choice = input("Enter your choice (1/2/3/4): ")
    
    
    if choice == '1':
        side = float(input("Enter the side length for square: "))
        s = Square(side)
        print("Area of square:", s.area())
    elif choice == '2':
        base = float(input("Enter the base length for triangle: "))
        height = float(input("Enter the height of the triangle: "))
        t = triangle(base, height)
        print("Area of triangle:", t.area())
    elif choice == '3':
        radius = float(input("Enter the radius of the circle: "))
        c = Circle(radius)
        print("Area of circle:", c.area())
    elif choice == '4':
        print("EXIT.")
        break
    else:
        print("Invalid choice. Please select a valid option.")

