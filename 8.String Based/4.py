'''
You are given a list of strings.Write a program to remove vowels from every string and print the new list.
Input Description:
First entry is the number of elements in the list.Then elements are enetered one below the other.
Sample Input:
4
cmrit
ece
vtu
aecs
Sample Output:
cmrt
c
vt
cs
'''

#Code starts here:
n=int(input())
list1=[]
list2=[]
for i in range(0,n):
    list1.append(input())

for i in list1:
    str2=''
    for j in i:
        if j not in 'AEIOUaeiou':
            str2=str2+j
    list2.append(str2)
print(*list2,sep='\n')
#Code ends here.
