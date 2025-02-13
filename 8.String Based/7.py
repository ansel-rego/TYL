'''
You are given a string. Write a program to print only the anagrams present in the string.
Anagrams means words containing same letters.
For Ex. listen and silent are anagrams.
Sample Input:
listen silent silent listen linest
Sample Output:
listen silent linest
'''

str1=input()
list1=str1.split()
list2=[]
for i in range((len(list1))-1):
    if sorted(list1[i])==sorted(list1[i+1]):
        if list1[i] not in list2:
            list2.append(list1[i])
        if list1[i+1] not in list2:
            list2.append(list1[i+1])
print(*list2)
