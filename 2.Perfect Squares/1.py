'''
Function should return either true or false if the input arguement is a perfect square 
Write a python function Is_Square to check whether given integer is perfect square or not.
Return True if yes, otherwise return False.
Sample Input:
9
Sample Output:
True
'''

#Code starts here:
n=int(input())
def Is_Square(n):
    n1=n**0.5
    n2=int(n1)
    n3=n2**2
    if (n3==n):
        return True
    else:
        return False
print(Is_Square(n))
#Code ends here.
