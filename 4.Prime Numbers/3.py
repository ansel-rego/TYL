'''
Write a python program to find all the prime number within a given interval.
Sample Input:
11 19
Sample Output:
11,13,17,19
'''

#Code starts here:
str1=input()
list1=str1.split()
list1=[int(i) for i in list1]
list2=[]
def Prime(num):
    if num<2:
        return False
    elif (num==2):
        return True
    else:
        for i in range (2,num):
            if (num%i==0):
                return False
        return True
    
for i in range(list1[0],list1[1]+1):
    if (Prime(i)==True):
        list2.append(i)

print(*list2,sep=',')
#Code ends here.
