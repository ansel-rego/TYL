'''
You are given several strings containing Os and 1s.
O indicates an empty parking space and 1 indicates an occupied parking space.
Imagine a new vehicle enters the parking lot.
Write a Python program to allot parking space in the row which contains maximum number of empty slots.
In case two rows have equal number of empty slots, then the program should choose the row which appears first in the list.#
In case there are no empty space for parking, then print "None".
Input Description: 
First integer represents the number of rows. Then the strings are entered one below the other.
Sample Input:
4
10101100
11001111
10000111
10010110
Sample Output:
1
'''

#Code starts here:
n = int(input())
list1=[]
list2=[]
for i in range(n):
    list1.append(input())
for i in list1:
    c=i.count("0")
    list2.append(c)
m=max(list2)
if m==0:
    print('None')
else:
    for i in range(len(list2)):
        if m==list2[i]:
            print(i+1)
            break
#Code ends here.
