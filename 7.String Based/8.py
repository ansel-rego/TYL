'''
You are given a sentence. Write a Python program to remove the non-repeated words of length greater than 5
Sample Input:
cmr institute institute of technology 
Sample Output:
cmr institute institute of
'''

str1=input()
list1=str1.split()
list2=[]

for i in list1:
    if list1.count(i)==1 and len(i)>5:
        list2.append(i)

print(*list2)