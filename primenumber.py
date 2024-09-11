#Prime number function 
num=int(input())

def Fun_Prime(num):
    if num<2:
        return False
    elif (num==2):
        return True
    else:
        for i in range (2,num):
            if (num%i==0):
                return False
        return True
        
print(Fun_Prime(num))

#You are given a list of integers. Write a Python program to print only the prime numbers present in the list. If there are no prime numbers in the list, then print 'NIL'

str1=input()
list1=str1.split(',')
list1=[int(i) for i in list1]
list2=[]

def Prime(num):
    if num<2:
        return False
    elif (num==2):
        return True
    else:
        for i in range (2,num):
            if (num%i==0):
                return False
        return True
    
for i in list1:
    if Prime(i)==True:
        list2.append(i)

if len(list2)==0:
    print ('Nil')
    
print(*list2,sep=',')

#Write a python program to find all the prime number within a given interval 

str1=input()
list1=str1.split()
list1=[int(i) for i in list1]
list2=[]
def Prime(num):
    if num<2:
        return False
    elif (num==2):
        return True
    else:
        for i in range (2,num):
            if (num%i==0):
                return False
        return True
    
for i in range(list1[0],list1[1]+1):
    if (Prime(i)==True):
        list2.append(i)

print(*list2,sep=',')

#Write a python program to generate the next 10 prime numbers starting from a given nmuber.
n=int(input())
list1=[]

def Prime(num):
    if num<2:
        return False
    elif (num==2):
        return True
    else:
        for i in range (2,num):
            if (num%i==0):
                return False
        return True

while (len(list1)<10):
    if Prime(n)==True:
        list1.append(n)
    n=n+1

print(*list1,sep='\n')