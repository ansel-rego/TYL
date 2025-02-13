'''
Write a Python program to generate next 10 perfect squares starting from the given number.
Sample Input:
9
Sample Output:
9,16,25,36,49,64,81,100,121,144
'''

def Is_Square(x):
    import math
    if int(math.sqrt(x))==(x**0.5):
        return True
    else:
        return False

n=int(input())
list1=[]

while len(list1)<10:
    if Is_Square(n):
        list1.append(n)
    n+=1

print(*list1,sep=',')