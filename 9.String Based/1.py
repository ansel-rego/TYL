'''
You are given a list of strings. Write a Python program to print only thr wonderful strings.
A wonderful string is a string which is made up of exactly three diffeent letters.
Print "None" if there are no wonderful strings in the given list.
Sample Input:
abca pqrs tuvt xyz
Sample Output:
abca tuvt xyz
'''

str1=input()
list1=str1.split()
list2=[]
for i in list1:
    if len(set(i))==3:
        list2.append(i)
if len(list2)!=0:
    print(*list2)
else:
    print('None')