# Create a class "Rectangle" and return the area and perimeters.

class Rectangle:
    def __init__(self, heigth, width):
        self.heigth = heigth
        self.width = width
    
    def return_area(self):
        return self.heigth * self.width
    def return_perimeter(self):
        return 2 * self.heigth + 2 * self.width
    
    @classmethod
    def square(cls, side):
        return cls(side, side)

rectangle_1 = Rectangle(4, 6)
print("Area:", rectangle_1.return_area())
print('Perimeter:', rectangle_1.return_perimeter())

recatangle_2 = Rectangle.square(6)
print('Area of the square: ', recatangle_2.return_area())