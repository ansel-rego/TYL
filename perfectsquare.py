# function should return either true or false if the input arguement is a perfect square 
# Write a python function Is_Square to check whether given integer is perfect square or not 
n=int(input())
def Is_Square(n):
    n1=n**0.5
    n2=int(n1)
    n3=n2**2
    if (n3==n):
        return True
    else:
        return False
print(Is_Square(n))

# Write a python program to print only the perfect squares present in the list. If there are no perfect squares, print 'NIL'
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


# Write a python program to generate perfect squares within a given interval.
# Print "NIL" if there are no perfect squares within the given interval 
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

print(*list2,sep='\n')

# Write a python program to generate next 10 perfect squares starting from the given number
def Is_Square(n):
    n1=n**0.5
    n2=int(n1)
    n3=n2**2
    if (n3==n):
        return True
    else:
        return False

n=int(input())
list1=[]

while (len(list1)<10):
    if (Is_Square(n)==True):
        list1.append(n)
    n+=1

print(*list1,sep=',')