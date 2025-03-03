'''
You are given a list of integers.
Write a python program to print only even numbers present in a list one below the other
Input Description : First integer represents the number of elements in the list.
Then the elements are entered one below the other.
Sample Input:
4
1
2
3
4
Sample Output:
2
4
'''

#Code starts here:
n = int(input())
list1=[]
for i in range(n):
    list1.append(int(input()))

even=[]

for i in list1:
    if (i%2==0):
        even.append(i)

print(*even,sep='\n')
#Code ends here.
