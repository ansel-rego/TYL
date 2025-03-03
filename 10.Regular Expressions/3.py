'''
You are given a list of strings. Write a Python program to print only valid Vehicle Numbers from the list. If there are no valid Vehicle Numbers, then print 'Nil'.
For Ex. KA63KN2024 is a valid vehicle number.
A valid vehicle number contains 2 letters followed by 2 digits followed by two letters and then 4 digits
Input Description:
First Input tells the number of strings. Then the list elements are entred one below the other.

Sample INPUT:
4
KA63HJ2024
KA63HJ202
A63HJ2024
KA63HJ2032

Sample OUTPUT:
KA63HJ2024
KA63HJ2032
'''

#Code starts here:
import re
n = int(input())
list1=[]
list2=[]
for i in range(n):
    list1.append(input())

sp=re.compile('^[A-Z]{2}(\d){2}[A-Z]{2}(\d){4}$')

for i in list1:
    if sp.search(i):
        list2.append(i)

if len(list2)!=0:
    print(*list2,sep='\n')
else:
    print('Nil')
#Code ends here.
