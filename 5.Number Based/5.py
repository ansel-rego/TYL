'''
Write a python fuction "LCM()" whick takes two numbers and returns their LCM
Sample Input:
6 4
Sample Output:
12
'''

#Code starts here:
str1=input()
list1=str1.split()
list1=[int(i) for i in list1]
a=list1[0]
b=list1[1]
def LCM(n1,n2):
    n3=max(n1,n2)
    n4=min(n1,n2)
    for i in range(1,(n3*n4)+1):
        if i%n3==0 and i%n4==0:
            return i
print(LCM(a,b))
#Code ends here.
