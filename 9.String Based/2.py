'''
#You are given a list of strings. Write a Python program to print only those strings which start with "Hello" and end with a digit.
Input Description:
First entry tells the number of strings.Then the strings are entered one below the other 
Sample Input:
4
Hello good morning 9
Hello how are you 8
Hi Hello 
Wassup 7
Sample Output:
Hello good morning 9
Hello how are you 8
'''

n=int(input())
list1=[]
list2=[]
for i in range(n):
    list1.append(input())

for i in list1:
    if i.startswith("Hello") or i.endswith("0123456789"):
        list2.append(i)

print(*list2,sep='\n')