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

#Code starts here:
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
#Code ends here.
