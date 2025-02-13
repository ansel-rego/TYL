'''
You are given a list of integers. Write a Python program to output a dictionary with the numbers as keys and their frequency of occurances as values.
Arrange the dictionary elements in the ascending order of their keys.
Sample Input:
2,2,4,4,2,6,6,4,6,8,8,8
Sample Output:
{2: 3, 4: 3, 6: 3, 8: 3}
'''


str1=input()
list1=str1.split(',')
list1=[int(i) for i in list1]
dict1={}
for i in sorted(list1):
    key=i
    dict1[key]=list1.count(i)
print(dict1)