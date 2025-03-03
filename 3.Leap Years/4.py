'''
You are given a integer. Write a python program to print the next 10 leap years starting from the given year
Sample Input:
100
Sample Output:
104,108,112,116,120,124,128,132,136,140

'''

#Code starts here:
n=int(input())
list1=[]

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
        
while (len(list1)<10):
    if (leap(n)==True):
        list1.append(n)
    n+=1

print(*list1,sep=',')
#Code ends here.
