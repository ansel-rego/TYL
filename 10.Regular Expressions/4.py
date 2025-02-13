'''
You are given a sentence. Write a program to extract the valid phone numbers present in the sentence. If there is no valid phone number, then print 'Nil'.
For Ex. 080-2847-4463 is a valid phone number
Sample INPUT:
CMRIT Bengaluru's ECE Dept's phone number is 080-2847-4463
Sample OUTPUT:
080-2847-4463
'''


str1=input()
import re
list1=str1.split()
list2=[]
sp=re.compile('^(\d){3}\-(\d){4}\-(\d){4}$')

for i in list1:
    if sp.search(i):
        list2.append(i)

if len(list2)!=0:
    print(*list2)
else:
    print('Nil')
