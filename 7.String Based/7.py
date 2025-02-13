'''
You are given a sentence. Write a Python program to remove the repeated words of length greater than 5.
Sample Input:
cmrit ece ece department department
Sample Output:
cmrit ece ece department
'''

str1=input()
list1=str1.split()
list2=[]
for i in list1:
    if (i in list2 and len(i)>5):
        continue
    else:
        list2.append(i)
print(*list2)