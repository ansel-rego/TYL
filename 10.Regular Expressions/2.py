'''You are given a list of strings. Write a Python program to print only the valid PAN(Permanent Acoount Number) from the given list. If there are no valid PANs, then print 'Nil'.
A PAN contains 5 letters followed by 4 digits followed by 1 letter.
Input Description:
The first entry tells the number of strings.Then the strings are entered one below the other.

Sample INPUT:
4
BDDCH6708X
BDDCH6708
BDCH6708X
XVVFG9807T

Sample OUTPUT:
BDDCH6708X
XVVFG9807T
'''

#without using RegEx:
n = int(input())
list1=[]
for i in range(n):
    list1.append(input())

list2=[]
for i in list1:
    if len(i)==10 and i[0:5].isalpha() and i[5:9].isdigit() and i[-1].isalpha():
        list2.append(i)

if len(list2)!=0:
    print(*list2,sep='\n')
else:
    print('Nil')


#using RegEx:
import re
n = int(input())
list1=[]
list2=[]
for i in range(n):
    list1.append(input())

sp=re.compile('^[A-Z]{5}(\d){4}[A-Z]{1}$')

for i in list1:
    if sp.search(i):
        list2.append(i)

if len(list2)!=0:
    print(*list2,sep='\n')
else:
    print('Nil')