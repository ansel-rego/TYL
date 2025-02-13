'''
Write a Python fucntion "GCD()" which takes two numbers and returns their GCD
Sample Input:
12
8
Sample Output:
4
'''

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