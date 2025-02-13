'''
You are given an integer N.Write a Python Program to generate Fibonacci series numbers up to N.
Sample Input:
5
Sample Output:
0,1,1,2,3,5
'''

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