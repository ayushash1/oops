# In Python OOP we have two types of Variables

# The first is
# Instance Variable

# The second is
# Class(Static) Variable

class Car:

    wheels = 4    # This is a Class Variable / Static Variable

    def __init__(self):
        self.mil = 10  # This is a Instance Variable 🙂
        self.brnd = "BMW" # Instance



c1 = Car()
c2 = Car()

c2.brnd = "Toyota"
c2.mil = 8.8


Car.wheels = 3 # this is how it is changed 


print(c1.mil, c1.brnd, c1.wheels )
print(c2.mil, c2.brnd, c2.wheels )