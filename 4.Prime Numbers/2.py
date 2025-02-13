'''
You are given a list of integers. Write a Python program to print only the prime numbers present in the list.
 If there are no prime numbers in the list, then print 'NIL'
Sample Input:
1,2,3,4,5,6,7,8
Sample Output:
2,3,5,7

'''
str1=input()
list1=str1.split(',')
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
    
for i in list1:
    if Prime(i)==True:
        list2.append(i)

if len(list2)==0:
    print ('Nil')
    
print(*list2,sep=',')