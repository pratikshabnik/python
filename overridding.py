class polygon():
    def area(self):
        print("area")

    def perimeter(self):
         print("perimeter")


class Triangle(polygon):
    def area(self):
        print("area of triangle")

    def perimeter(self):
        print("perimeter of triangle")

class Square(polygon):
    def area(self):
        print("area of square")

    def perimeter(self):
        print("perimeter of square")


p = Triangle()
p.area()


s = Square()
s.perimeter()



