'''
You are given a list of words.Write a Python Program to print the word with highest number of vowels in it.
If two words have equal number of vowels, then select the word which appears first in the given list.
Input Description:
First entry is the number of elements in the list.Then elements are enetered one below the other.
Sample Input:
4
raveesh
kaveesh
mahesh
rajesh
Sample Output:
raveesh
'''

n=int(input())
list1=[]
for i in range(n):
    list1.append(input())
count_past=0
for i in list1:
    count_present=0
    for j in i:
        if j in 'AEIOUaeiou':
            count_present+=1
    if count_present>count_past:
        req_word=i
        count_past=count_present
print(req_word)