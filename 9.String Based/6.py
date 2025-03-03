'''
You are given a list of email IDs.Write a program to extract name of the employee and the name of the company.
Input description:
First integer gives the number of elements.The elements are entered one below the other.
Sample Input:
4
sachin@tcs.com
virat@infosys.com
rohit@wipro.com
rahul@reliance.com
Sample Output:
sachin,tcs
virat,infosys
rohit,wipro
rahul,reliance
'''


#Code starts here:
n=int(input())
list1=[]
for i in range(n):
    list1.append(input())

for i in list1:
    list2=i.split('@')
    list3=list2[1].split('.')
    print(list2[0],list3[0],sep=',')

#Code ends here.
