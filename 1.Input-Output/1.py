'''
You are given a list of integers
Write a python program to print only even numbers present in a list
Sample Input:
1 2 3 4 5 6
Sample Output:
2 4 6
'''
str1= input()
list1= str1.split()
list1 = [int(i) for i in list1]
list2=[]

for i in list1:
    if (i%2==0):
        list2.append(i)

print(*list2)