'''
Write a python program to generate the next 10 prime numbers starting from a given number.
Sample Input:
5
Sample Output:
5
7
11
13
17
19
23
29
31
37
'''

#Code starts here:
n=int(input())
list1=[]

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

while (len(list1)<10):
    if Prime(n)==True:
        list1.append(n)
    n=n+1
print(*list1,sep='\n')
#Code ends here.
