'''
Write a python fucntion "Spy()" to check whether a given number is Spy number or not. Print True if the number is a Spy Number. Otherwise print False.
A number is said to be a Spy number if the sum of all the digits is equal to the product of all digits.
Sample Input:
1412
Sample Output:
True
'''

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