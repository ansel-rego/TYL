#Write a Python function "Fun_Fib()" that takes an integer as input and generates a Fibonacci series of that length.
n=int(input()) 
def Fun_Fib(n):
    if n==1:
        list1=[0]
    elif n==2:
        list1=[0,1]
    else:
        list1=[0,1]
        while(len(list1)<n):
            next=list1[-1]+list1[-2]
            list1.append(next)
    print(*list1,sep=',')

Fun_Fib(n) 


#You are given an integer N.Write a Python Program to generate Fibonacci series numbers up to N.
n=int(input()) 
def Fun_Fib(n):
    if n==0:
        list1=[0,]
    elif n==1:
        list1=[0,1,1]
    else:
        list1=[0,1,1]
        next=list1[-1]+list1[-2]
        while(next<=n):
            list1.append(next)
            next=list1[-1]+list1[-2]
    print(*list1,sep=',')
Fun_Fib(n) 



#Write a Python function "Is_Fib()" which takes a number and return True if the number is a member of Fibonacci series.Otherwise, return False
n=int(input())
def Is_Fib(n):
    if n==0:
        return True
    elif n==1:
        return True
    else:
        list1=[0,1]
        next=list1[-1]+list1[-2]
        while(next<=n):
            if next==n:
                return True
            else:
                list1.append(next)
                next=list1[-1]+list1[-2]
        if next==n:
            return True
        else:
            return False
print(Is_Fib(n))


#Write a Python Program which takes a lower limit and an upper limit and prints the Fibonacci numbers in that interval 
lower=int(input())
upper=int(input())
if lower==0 and upper==1:
    list1=[0,1,1]
else:
    list1=[0,1]
    next=list1[-1]+list1[-2]
    list2=[]
    while(next<=upper):
        if next>=lower:
            list2.append(next)
        next=list1[-1]+list1[-2]
        list1.append(next)  
print(*list2)



#Write a Python Program to find the product of a list of numbers based on the following rules:
#1.If 5 is not present in the list,display the product of all the numbers
#If one of the integers is 5,display the product of numbers to the right of 5 excluding 5 and any subsequent 5's
#If there are no numbers to the right of 5, display -1
str1=input()
list1=str1.split()
list1=[int(i) for i in list1]
if 5 not in list1:
    prod=1
    for i in list1:
        prod=prod*i
    print(prod)
else:
    index1=list1.index(5)
    if index1+1==len(list1):
        print(-1)
    else:
        prod=1
        for i in range(index1+1,len(list1)):
            if i!=5:
                prod=prod*i
        print(prod)



#Some prime numbers are equal to the sum of other consecutive prime numbers.
#Write a Python program to print the prime numbers that satisfy this property up to a given number
n=int(input())
def prime(n):
    if (n<2):
        return False
    elif (n==2):
        return True
    else:
        for i in range(2,n):
            if n%i==0:
                return False
        return True
list1=[]
for i in range(2,n+1):
    if prime(i)==True:
        list1.append(i)
list2=[]
sum=0
for i in list1:
    sum=sum+i
    if sum in list1 and sum!=2:
        list2.append(sum)
print(*list2,sep='\n')