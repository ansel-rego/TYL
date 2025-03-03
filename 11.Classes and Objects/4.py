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

#Code starts here:
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
#Code ends here.
