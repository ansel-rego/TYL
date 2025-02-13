'''
Write a python program "Is_Armstrong()" to check whether a given number is Armstrong or not.Print True if the number is Armstrong number.Otherwise print False
Armstrong number is a number which is equal to sum of its digits raised to the number of digits present in that number.
Sample Input:
153
Sample Output:
True
'''

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