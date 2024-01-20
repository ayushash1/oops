
# Python does not support method overloading. We may overload the methods but can only use the latest defined method.

class Student:

    def __init__(self, m1, m2):
        self.m1 = m1
        self.m2 = m2

    def sum(self, a=None, b=None, c=None):
        s = 0

        if a != None and b !=None and c != None:
            s = a+b+c
        
        elif a!=None and b!=None:
            s = a+b
        
        else: 
            s=a

        return s



s1 = Student(34, 54)

print(s1.sum(4))