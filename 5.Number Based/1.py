'''
Write a python program to print the odd factors of a number. Arrange the output in ascending order.
Sample Input:
10
Sample Output:
1 5

'''

#Code starts here:
n=int(input())
list1=[]
for i in range(1,n+1):
    if (n%i==0) and (i%2!=0):
        list1.append(i)
print(*list1,sep=' ')
#Code ends here.
