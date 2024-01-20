
# Inheritance is like parent child relation
# we can make a child class B to access the methods of parent class A


class A:
    
    def feature1(self):
        print("feature1 working")
    
    def featuer2(self):
        print("feature2 working")

class B(A): # Made it the child class (or subclass) of class A
    
    def feature3(self):
        print("feature3 working")
    
    def featuer4(self):
        print("feature4 working")
    

class C(B): # Multi level 

    def feature5(self):
        print("feature5 is working")

    

a1 = A()

a1.feature1()
a1.featuer2()

b1 = B()

b1.feature1 # now can access methods of class A in class B instance
b1.feature3

c1 = C()

