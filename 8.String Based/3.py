'''
Your are give a string. Write a Python Program to print the number of uppercase and lowercase letters.
Sample Input:
Cmrit Ece 2000
Sample Output:
2,6
'''

str1=input()
counter_upper=0
counter_lower=0
for i in str1:
    if i.isupper():
        counter_upper+=1
    elif i.islower():
        counter_lower+=1
print(counter_upper,counter_lower,sep=',')