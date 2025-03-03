'''
Given a list. Write a python program to print only the leap years given in a list. Print 'NIL' if there are no leap years given in the list.
Sample Input:
100,104,108,400,404,408
Sample Output:
104,108,400,404,408
'''

#Code starts here:
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
#Code ends here.
