'''
Given a string, write a Python program to remove all the spaces and find their length.
Also, output whether the length is even or odd.
Sample Input:
vtu cmrit ece
Sample Output:
11 odd
'''

#Code starts here:
str1=input()
str2=str1.split()
str3=''.join(str2)
if len(str3)%2==0:
    print(len(str3),'even')
else:
    print(len(str3),'odd')
#Code ends here.
