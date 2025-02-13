'''
Write a function 'is_leap()' that takes a year as input and returns True if it is a leap year and returns False otherwise.
A leap year is deivisible by 4 except for century years. A century year is a leap year only if it is divisible by 400
Sample Input:
100
Sample Output:
False
'''

def is_leap(year):
    if (year % 400 == 0) and (year % 100 == 0):
        return True
    elif (year % 4 ==0) and (year % 100 != 0):
        return True 
    else:
        return False

#alternate method  
'''
def is_leap(n):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False
'''
    
print(is_leap())