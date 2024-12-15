'''
Write a python program to create a class representing a circle. Include methods to calculate its area and cirumference
Take redius of the circle as input from the user.
Sample Input:
3
Sample Output:
28.274333882308138
18.84955592153876
'''
class circle:
    def __init__(self,r):
        self.radius=r
    def area(self):
        import math
        A=(math.pi)*(self.radius**2)
        return A
    def circumference(self):
        import math
        C=2*(math.pi)*self.radius
        return C

r=int(input())
c=circle(r)

print(c.area())
print(c.circumference())



'''
Write a python program to create a class called 'Complex'.Each Complex object should have real part and imaginary part.
Include method to add two complex numbers.
Input Description:
First line contains real part and imaginary part of the first complex number.
Second line contains real part and imaginary part of the second complex number.
Sample Input:
2,4
1,3
Sample Output:
3 7
'''
class Complex:
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def add(self, other):
        return Complex(self.real+other.real, self.imaginary+other.imaginary)


# Input handling
if __name__ == "__main__":
    r1, i1 = map(int, input().split(','))
    r2, i2 = map(int, input().split(','))
    
    # Create Complex objects and add them
    result = Complex(r1, i1).add(Complex(r2, i2))
    
    # Print the result
    print(result.real, result.imaginary)





'''
Write a python program to create a class called 'Complex'.Each Complex object should have real part and imaginary part.
Include method to find the magnitude and phase of the complex number.
Hint1: Use round(x,4) function to limit the decimal value to 4 positions.
Hint2: Import math module and use math,atan2(imaginary_part,real_part) function to find the phase of the complex number.
Hint3: Magnitude of the complex number is equal to square root of (real_part^2+imaginary_part^2)
Input Description: First line comtains real part and imaginary part of the complex number seperated by comma.
Sample Input:
2,3
Sample Output:
3.6056
0.9828
'''
class complex:
    def __init__(self,r,i):
        self.real=r
        self.imaginary=i
    def magnitude(self):
        M=(self.real**2+self.imaginary**2)**0.5
        return round(M,4)
    def phase(self):
        import math
        P=math.atan2(self.imaginary,self.real)
        return round(P,4)

str1=input()
list1=str1.split(',')
c=complex(float(list1[0]),float(list1[1]))

#This line cannot be edited
print(c.magnitude())
print(c.phase())





'''
Write a Python program to create a class called 'Student'.
Include methods to find the percentage and SGPA of the student.
Consider marks scored by the student in three subjects out of 50.
SGPA=(Percentage/10)+0.75
If the calculated SGPA is greater than 10, consider SGPA as 10.0
Hint: Use round(x,2) function to limit the decimal value to 2 positions.
Input Description: First line contains marks scored by the student in three subjects out of 50, seperated by comma.
Sample Input:
35,42,44
Sample Output:
80.67
8.82
'''
str1=input()
list1=str1.split(',')
list1=[int(i) for i in list1]

class Student:
    def __init__(self,m1,m2,m3):
        self.marks1=m1
        self.marks2=m2
        self.marks3=m3
    def Percentage(self):
        per = (self.marks1+self.marks2+self.marks3)*(100/150)
        return round(per,2)
    def SGPA(self):
        sgpa=((self.Percentage()/10)+0.75)
        if sgpa>10:
            return 10.00
        return round(sgpa,2)


Raveesh = Student(list1[0],list1[1],list1[2])

print(Raveesh.Percentage())
print(Raveesh.SGPA())



'''
Write a Python program to create a class called 'Employee'. Include methods to calculate monthly salary to be paid and update the remaining. Take actual salary and number of leaves takes as input from the user.
Monthly Salary to be Paid=90% of Actual Salary 
10% of salary deducted as tax.
leaves Remaining=12-Number of leaves taken.
Input Description:
First number is the actual salary. Second number is the number of leaves taken.
Sample Input:
100000 2
Sample Output:
90000
10
'''
str1=input()
list1=str1.split()
list1=[int(i) for i in list1]

class Employee:
    def __init__(self,s,l):
        self.salary=s
        self.leaves=l
    def Salary(self):
        month_sal=self.salary*0.9
        return int(month_sal)
    def Leaves(self):
        l = 12-self.leaves
        return l

Raveesh = Employee(list1[0],list1[1])

print(Raveesh.Salary())
print(Raveesh.Leaves())


'''
Write a Python program to create a class called 'Rectangle'.Include methods to calculate area of a rectange and the lenght of the diagonal.
Take the length of the sides as input from the user.
Use round(x,2) function to limit the decimal value to 2 positions.
Sample Input:
2,3
Sample Output:
6
3.61
'''
class rectangle():
    def __init__(self,l,b):
        self.length=l
        self.breadth=b
    def area(self):
        A=self.length*self.breadth
        return round(A,2)
    def diagonal(self):
        D=(((self.length)**2)+((self.breadth)**2))**0.5
        return round(D,2)

s=input()
list1=s.split(',')
rect=rectangle(int(list1[0]),int(list1[1]))

print(rect.area())
print(rect.diagonal())
