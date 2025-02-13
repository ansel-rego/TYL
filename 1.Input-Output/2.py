# The * symbol is used to print the list elements in a single line with space.
# To print all elements in new lines or separated by comma use sep=”\n” or sep=”, ” respectively. 

'''
You are given a list of integers
Python program to print only even numbers present in a list seperated by commas
Sample Input:
1,2,3,4,5,6
Sample Output:
2,4,6
'''
str1=input()
list1=str1.split(',')
list1=[int(i) for i in list1]

even=[]

for i in list1:
    if (i%2==0):
        even.append(i)
    
print(*even,sep=',')

