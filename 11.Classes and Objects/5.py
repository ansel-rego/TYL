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

#Code starts here:
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
#Code ends here.

