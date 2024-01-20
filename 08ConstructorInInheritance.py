
# MRO ?

class A:

    def __init__(self):
        print("in Innit of A")
    
    def feature1(self):
        print("feature1 working")
    
    def featuer2(self):
        print("feature2 working")

class S:

    def __init__(self):
        print("in innit of S")

    def meth1(self):
        super().feature1() # using super() method

# When we dont have constructor of B it uses parents constructor
# And if we have constructor of B it wont use constructor of parent
class B(A): # Made it the child class (or subclass) of class A
    
    def __init__(self):
        super().__init__()  # by doing this we are using / calling constructor of A too
        print("in Innit of B")

    def feature3(self):
        print("feature3 working")
    
    def featuer4(self):
        print("feature4 working")


class C(A, S):

    def __init__(self):
        super().__init__()  # this would call __init__ A only, because of MRO( Method Resolution Order) which is left to right


a1 = C()  # a1 is a obj variable or an instance

