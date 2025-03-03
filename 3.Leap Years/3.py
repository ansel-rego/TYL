'''
You are given two integers (lower and upper). Write a python program to find all the leap years in the given interval 
Sample Input:
100
120
Sample Output:
104
108
112
116
120
'''

#Code ends here.
lower=int(input())
upper=int(input())
def leap(year):
    if (year%4!=0):
        return False
    else:
        if (year%400==0):
            return True
        elif (year%100==0):
            return False
        else:
            return True
        
for i in range(lower,upper+1):
    if (leap(i)==True):
        print(i)
#Code ends here.
