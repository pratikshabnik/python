class Parent:
    def Data(self):
        print("parent data")

class Child(Parent):
    def Data1(self):
        print("child data")

c = Child()
c.Data()
c.Data1()