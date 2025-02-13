'''
You are given a list of unique names.Write a Python program to print the names that start with "R" or "r" and end with "H" or "h".
If there are no such names, print -1.
Sample Input:
Raveesh,rajesh,mahesh,Rakesh
Sample Output:
Raveesh
rajesh
Rakesh
'''

str1=input()
list1=str1.split(',')
list2=[]
for i in list1:
    if i[0]=='R' or i[0]=='r':
        if i[-1]=='H' or i[-1]=='h':
            list2.append(i)   

if (len(list2)==0):
    print(-1)
else:
    print(*list2,sep='\n')

