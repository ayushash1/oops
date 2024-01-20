

class Computer:
    # Methods (not functions)

    # default constructor 
    def __init__(self):
        self.name = "Ayush"
        self.age = 21

    # method of defining age
    def update(self):
        self.age = 22

    def compareAge(self, other):
        if self.age == other.age:
            return True
        else:
            return False



c1 = Computer() 
c2 = Computer()

c2.name = "idk"
c2.age = 18

c1.update() # self is a pointer in this case self is dircting object to "c1" which is called here

# Size of an Object? = Depends on the no. of Variables of each Variable
# Who allocates size to object? = Constructor

if c1.compareAge(c2): # when we call c1.compare c1 becomes self and c2 becomes other (look at compare object)
    print("They are same age")
else:
    print("They are not same age")

print(c1.name)
print(c2.name)