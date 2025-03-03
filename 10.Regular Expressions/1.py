'''You are given a list of strings. Write a Python program to output only valid USNs from the given list. If there are no valid USNs, then print 'Nil'.
A valid USN contains exactly 10 characters out of them 1st character is a digit, the next 2 characters are alphabetical characters, then two digits, then 2 alphabetical characters, then 3 digits.
Sample INPUT:
4
1CR22EC285
CR22EC285
1CR22EC2894
1CR22EC286

Sample OUTPUT:
1CR22EC285
1CR22EC286
'''

#without using RegEx:
#Code starts here:
n=int(input())
list1=[]
list2=[]

for i in range(n):
    list1.append(input())

for i in list1:
    if len(i)==10 and i[0].isdigit() and i[1:3].isalpha() and i[3:5].isdigit() and i[5:7].isalpha() and i[7:].isdigit():
        list2.append(i)

if len(list2)!=0:
    print(*list2,sep='\n')
else:
    print('Nil')
#Code ends here.


#using RegEx:
#Code starts here:
import re
n=int(input())
list1=[]
list2=[]
for i in range(n):
    list1.append(input())

sp=re.compile('^(\d){1}[A-Z]{2}(\d){2}[A-Z]{2}(\d){3}$')

for i in list1:
    if sp.search(i):
        list2.append(i)

if len(list2)!=0:
    print(*list2,sep='\n')
else:
    print('Nil')
#Code ends here.
