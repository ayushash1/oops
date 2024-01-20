# Class = Design or BluePrint
# Object = Instance

# Classes and Object in Python
# If we want an Object we need a Class (Blueprint)

class Computer:
    # Attributes ->(Variables), 
    # And Behavior -> Methods (Function)
    
    # this is constructor
    def config(self): # this is called a METHOD not FUNCTION
        print("i5 machine with 8 gb ram and 512gb ssd")


# Creating Object of the class
comp1 = Computer()
comp2 = Computer()

# print(type(comp1))

Computer.config(comp1)
Computer.config(comp2)

comp1.config() # Normal Syntax
comp2.config()

a = 5
a.bit_length()