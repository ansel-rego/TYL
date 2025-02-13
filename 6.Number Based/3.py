'''
Write a Python function "Is_Fib()" which takes a number and return True if the number is a member of Fibonacci series.Otherwise, return False
Sample Input:
5
Sample Output:
True
'''

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