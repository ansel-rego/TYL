'''
Write a function 'Fun_Prime()' that takes a number and returns True if it is prime and returns False otherwise.
Sample Input:
5
Sample Output:
True
'''

num=int(input())

def Fun_Prime(num):
    if num<2:
        return False
    elif (num==2):
        return True
    else:
        for i in range (2,num):
            if (num%i==0):
                return False
        return True
        
print(Fun_Prime(num))

#althernate method
'''
def Fun_Prime(n):
    import math
    if (n==0 or n==1):
        return False
    elif(n==2):
        return True
    else:
        for i in range(2,int(math.sqrt(n)+1)):
            if (n%i==0):
                return False
        return True
'''