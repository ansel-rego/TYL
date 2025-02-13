'''
Write a Python program to convert a given decimal number into an equivalent binary number 
Sample Input:
11
Sample Output:
1011
'''

n=int(input())
str1=''
while(n>0):
    r=n%2
    str1=str(r)+str1
    n=n//2
print(str1)