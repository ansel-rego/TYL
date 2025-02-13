'''
Write a python program to generate perfect squares within a given interval.
Print "NIL" if there are no perfect squares within the given interval 
Sample Input:
10,50
Sample Output:
16
25
36
49
'''

def Is_Square(n):
    n1=n**0.5
    n2=int(n1)
    n3=n2**2
    if (n3==n):
        return True
    else:
        return False

str1=input()
list1=str1.split(',')
list1=[int(i) for i in list1]
list2=[]

for  i in range(list1[0],list1[1]+1):
    if (Is_Square(i)==True):
        list2.append[i]

if len(list2)==0:
    print('NIL')
else:
    print(*list2,sep='\n')