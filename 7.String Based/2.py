'''
You are given a list of words. Write a Python program to print only the palindromes present in the list.
If there are no palindromes in the given list,then print "Nil"
Sample Input:
4
radar
nation
team
madam
Sample Output:
radar
madam
'''

#Code starts here:
n=int(input())
list1=[]
list2=[]
for i in range (0,n):
    list1.append(input())
for i in list1:
    if i==i[::-1]:
        list2.append(i)
if len(list2)==0:
    print('Nil')
else:
    print(*list2,sep='\n')

#Code ends here.
