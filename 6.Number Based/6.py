'''
Some prime numbers are equal to the sum of other consecutive prime numbers.
For Example 5=2+3
17=2+3+5+7, 
41=2+3+5+7+11+13
Write a Python program to print the prime numbers that satisfy this property up to a given number.
Sample Input:
50
Sample Output:
5
17
41
'''

#Code starts here:
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
#Code ends here.
