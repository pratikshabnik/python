class Father:
    fathername = "Bajarang"

class Mother:
    mothername = "Anita"

class Daughter(Father,Mother):
    def Data(self):
        print("Father Name: ",self.fathername)
        print("Mother name: ",self.mothername)

d=Daughter()
d.Data()

