'''
You are given a list of strings.Write a Python program to print only the valid IP addresses from the list.
A valid IP address contains four numbers ranging from 0 ti 255 seperated by a dot.
A number cannot start with 0 unless 0 is the only digit in that number.
if there are no valid IP addresses in the list,print "Nil".
Input Description:
Frist integer tells the number of elements in the list.
Then the elements are enetered one below the other
Sample INPUT:
4
192.168.0.1
292.168.0.1
192.168.02.1
192.16.0.1
Sample OUTPUT:
192.168.0.1
192.16.0.1
'''

n=int(input())
import re
list1=[]
for i in range(n):
    list1.append(input())
sp=re.compile('^((25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.){3}(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])$')
list2=[]
for i in list1:
    if sp.search(i):
        list2.append(i)

if len(list2)!=0:
    print(*list2,sep='\n')
else:
    print('Nil')
