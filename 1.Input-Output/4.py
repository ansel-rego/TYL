'''
You are given a list of words
Write a Python Program to print only the odd length word 
Sample Input:
Rohit Virat Hardik Bumra
Sample Output:
Rohit Virat Bumra
'''

str1=input()
list1 = str1.split()

words=[]

for i in list1:
    if (len(i)%2!=0):
        words.append(i)

print(*words)