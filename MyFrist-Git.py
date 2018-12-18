'''
Created on 19-Dec-2018

@author: Dileep
'''
# Inheritance

#Parent Class
class A:
    def feature1(self):
        print("Feature 1 is working on Class A")
    
    def feature2(self):
        print("Feature 2 is working on Class A")

# Single Inheritance
class B(A):
    def feature3(self):
        print("feature 3 is working on Class B")
    
    def feature4(self):
        print("feature 4 is working on Class B")

# Multilevel Inheritance         
class C(B):
    def feature5(self):
        print("feature 5 is working on Class C")
        
#Parent Class
class X:
    def feature3(self):
        print("Feature 3 is working on Class X")
        
    def feature4(self):
        print("feature 4 is working on Class X")

# Multiple Inheritance
class Y(A,X):
    def feature5(self):
        print("feature 5 is working on Class Y")

print("# Parent Class")
a = A()
a.feature1()
a.feature2()
print()

# Single Inheritance
print("# Single Inheritance")
b= B()
b.feature1()
b.feature2()
b.feature3()
b.feature4()
print()

# Multilevel Inheritance 
print("# Multilevel Inheritance")
c = C()
c.feature1()
c.feature2()
c.feature3()
c.feature4()
c.feature5()
print()

# Multiple Inheritance
print("# Multiple Inheritance")
y = Y()
y.feature1()
y.feature2()
y.feature3()
y.feature4()
y.feature5()
