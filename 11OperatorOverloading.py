

# a = 5
# b = 6
# print(a+b)


# # magic methods
# int.__add__(a,b)


class Students:
    def __init__(self, m1, m2):
        self.m1 = m1
        self.m2 = m2

    def __add__(self, other):  # overloading operator (in this case +) so that my class knows what to do when + is called
        m1 = self.m1 + other.m1
        m2 = self.m2 + other.m2
        s3 = Students(m1, m2)

        return s3
    
    def __gt__(self, other):
        s1 = self.m1 + self.m2
        s2 = other.m2 + other.m2

        if s1 > s2:
            return True
        else: return False
    
    def __str__(self):
        # return f'{self.m1} {self.m2}'
        return f'{self.m1} {self.m2}'

    

s1 = Students(85, 67)
s2 = Students(76, 32)

s3 = s1 + s2

if s1 > s2:
    print("S1 wins")
else:
    print("S2 wins")

a = 9
print(a.__str__())

print(s1)