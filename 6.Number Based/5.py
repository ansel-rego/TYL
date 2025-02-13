'''
Write a Python Program to find the product of a list of numbers based on the following rules:
1.If 5 is not present in the list,display the product of all the numbers
2.If one of the integers is 5,display the product of numbers to the right of 5 excluding 5 and any subsequent 5's
3.If there are no numbers to the right of 5, display -1.
Sample Input:
1 2 5 3 4
Sample Output:
12
'''

str1=input()
list1=str1.split()
list1=[int(i) for i in list1]
if 5 not in list1:
    prod=1
    for i in list1:
        prod=prod*i
    print(prod)
else:
    index1=list1.index(5)
    if index1+1==len(list1):
        print(-1)
    else:
        prod=1
        for i in range(index1+1,len(list1)):
            if i!=5:
                prod=prod*i
        print(prod)