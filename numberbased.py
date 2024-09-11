#write a python program to print the odd factors of a number. arrange the output in ascending order.
n=int(input())
list1=[]
for i in range(1,n+1):
    if (n%i==0) and (i%2!=0):
        list1.append(i)
print(*list1,sep=' ')

#Write a python program that takes a list of integers, removes duplicates and prints only unique numbers present in the given list.Skip numbers deivisible by 3.  Arrange the output in ascending order. The elements are enetered one below the other 
n=int(input())
list1=[]
list2=[]
for i in range(n): 
    list1.append(int(input()))
for i in list1:
    if i not in list2 and i%3!=0:
        list2.append(i)
    
print(*list2,sep='\n')

#Write a Python program that takes a list of numbers and prints only those numbers which are not repeated.If there are non-repeated numbers,print "None". The elements are entered one below the other 
n=int(input())
list1=[]
list2=[]
for i in range(n):
    list1.append(int(input()))
for i in list1:
    if list1.count(i)==1:
        list2.append(i)
if len(list2)==0:
    print("None")
else:
    print(*list2,sep='\n')

#Write a Python program that takes an integer as input and form a new number which has the least significant digit of the original number in its one's place and totoal number of digits of the original number in its ten's place
n=int(input())
l=len(str(n))
m=n%10
new=str(l)+str(m)
print(new)

#Write a python fuction "LCM()" whick takes two numbers and returns their LCM
list1=input()
list1=list1.split()
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


#Write a Python fucntion "GCD()" which takes two numbers and returns their GCD
num1=int(input()) 
num2=int(input()) 
def GCD(n1,n2):
    larger=max(n1,n2)
    smaller=min(n1,n2)
    for i in range(1,smaller+1):
        if (n1%i==0) and (n2%i==0):
            gcd=i
    return gcd
            
print(GCD(num1,num2)) 

#Write a python program "Is_Armstrong()" to check whether a given number is Armstrong or not.Print True if the number is Armstrong number.Otherwise print False
#Armstrong number is a number which is equal to sum of its digits raised to the number of digits present in that number 
n=int(input())
def Is_Armstrong(n):
    l=len(str(n))
    sum=0
    for i in (str(n)):
        sum=sum+(int(i)**l)
    if sum==n:
        return True
    else:
        return False
print(Is_Armstrong(n)) 

#Write a python fucntion "Spy()" to check whether a given number is Spy number or not. Print True if the number is a Spy Number. Otherwise print False
#A number is said to be a Spy number if the sum of all the digits is equal to the product of all digits
n=int(input())
def Spy(n):
    s=str(n)
    sum=0
    product=1
    for i in s:
        sum=sum+int(i)
        product=product*int(i)
    if product==sum:
        print("True")
    else:
        print("False")
Spy(n) 

#Write a Python program to convert a given decimal number into an equivalent binary number 


#Write a Python program to convert the given binary number to its equivalent decimal number.