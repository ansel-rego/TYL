def is_leap(year):
    if (year % 400 == 0) and (year % 100 == 0):
        return True
    elif (year % 4 ==0) and (year % 100 != 0):
        return True 
    else:
        return False
    
print(is_leap())

#Given a list. Write a python program to print only the leap years given in a list. Print 'NIL' if there are no leap years given in the list
str1=input()
list1=str1.split(',')
list1=[int(i) for i in list1]  

def is_leap(year):
    if (year % 400 == 0) and (year % 100 == 0):
        return True
    elif (year % 4 ==0) and (year % 100 != 0):
        return True 
    else:
        return False

list2=[]
for i in list1:
    if (is_leap(i)==True):
        list2.append(i)

if len(list2)==0:
    print('NIL')
   
print(*list2,sep=',')

#You are given two integers (lower and upper). Write a python program to find all the leap years in the interval 
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


#You are given a integer. Write a python program to print the next 10 leap years starting from the given year
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

