'''
You are given a string.Write a Python program to print the number of alphabetical characters,digits,spaces,special characters.
Sample Input:
Cmrit Ece 2000 @#$
Sample Output:
8,4,3,3
'''

#Code starts here:
str1=input()
alphabet=0
digits=0
spaces=0
specialchar=0
for i in str1:
    if i.isalpha():
        alphabet+=1
    elif i.isdigit():
        digits+=1
    elif i.isspace():
        spaces+=1
    else:
        specialchar+=1
print(alphabet,digits,spaces,specialchar,sep=',')
#Code ends here.
