'''
You are given a string.
Write a Python program to find the number of vowels and consenants present in the string.
Sample Input:
Cmrit Ece 2000
Sample Output:
3,5
'''

#Code starts here:
str1=input()
counter_c=0
counter_v=0
for i in str1:
    if i.isalpha():
        if i in 'AEIOUaeiou':
            counter_v+=1
        else:
            counter_c+=1
print(counter_v,counter_c,sep=',')
#Code ends here.
