'''
You are given a list of integers.
Write a python program to print only the perfect squares present in the list. If there are no perfect squares, print 'NIL
Ig there are no perfect squares, print 'Nil'
Sample Input:
1,2,3,4,5,6,7,8,9,10
Sample Output:
1
4
9
'''

str1=input()
list1=str1.split(',')
list1=[int(i) for i in list1]

def Is_Square(n):
    n1=n**0.5
    n2=int(n1)
    n3=n2**2
    if (n3==n):
        return True
    else:
        return False

list2=[]
for i in list1:
    if (Is_Square(i)==True):
        list2.append(i)

if len(list2)==0:
    print ('NIL')
    
print(*list2,sep='\n')