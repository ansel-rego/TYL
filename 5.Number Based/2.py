'''
Write a python program that takes a list of integers, removes duplicates and prints only unique numbers present in the given list.
Skip numbers divisible by 3.
Arrange the output in ascending order. The elements are enetered one below the other.
Input Description:
First Input tells the number of elements. Then elements are entered one below the other.
Sample Input:
6
10
11
12
10
11
12
Sample Output:
10
11
'''

n=int(input())
list1=[]
list2=[]
for i in range(n): 
    list1.append(int(input()))
for i in list1:
    if i not in list2 and i%3!=0:
        list2.append(i)
    
print(*list2,sep='\n')