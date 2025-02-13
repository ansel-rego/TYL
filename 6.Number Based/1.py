'''
Write a Python function "Fun_Fib()" that takes an integer as input and generates a Fibonacci series of that length.
Sample Input:
5
Sample Output:
0,1,1,2,3
'''

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
