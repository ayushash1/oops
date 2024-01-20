

class student:
    def __init__(self, name , rolno):
        self.name = name
        self.rolno = rolno
        self.lap = self.Laptop()

    def show(self):
        print(self.name, self.rolno)
        self.lap.show()


    class Laptop:
        
        def __init__(self):
            self.brand = "HP"
            self.cpu = "i5"
            self.ram = "8g"

        def show(self):
            print(self.brand, self.cpu, self.ram)

s1 = student(name="ayush", rolno=1)
s2 = student(name="idk", rolno=2)

s1.show()
