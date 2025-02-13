'''
Write a Python Program which takes a lower limit and an upper limit and prints the Fibonacci numbers in that interval 
Sample Input:
5
34
Sample Output:
5 8 13 21 34
'''

lower=int(input())
upper=int(input())
if lower==0 and upper==1:
    list1=[0,1,1]
else:
    list1=[0,1]
    next=list1[-1]+list1[-2]
    list2=[]
    while(next<=upper):
        if next>=lower:
            list2.append(next)
        next=list1[-1]+list1[-2]
        list1.append(next)  
print(*list2)