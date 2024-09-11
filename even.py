# Python program to print only even numbers present in a list
str1= input()
list1= str1.split()
list1 = [int(i) for i in list1]
list2=[]

for i in list1:
    if (i%2==0):
        list2.append(i)

print(*list2)

# The * symbol is used to print the list elements in a single line with space.
# To print all elements in new lines or separated by comma use sep=”\n” or sep=”, ” respectively. 

# Python program to print only even numbers present in a list seperated by commas
str1=input()
list1=str1.split(',')
list1=[int(i) for i in list1]

even=[]

for i in list1:
    if (i%2==0):
        even.append(i)
    
print(*even,sep=',')


# Python program to print only even numbers present in a list one below the other
n = int(input())
list1=[]
for i in range(n):
    list1.append(int(input()))

even=[]

for i in list1:
    if (i%2==0):
        even.append(i)

print(*even,sep='\n')


# Write a Python Program to print only the odd length word 
str1=input()
list1 = str1.split()

words=[]

for i in list1:
    if (len(i)%2!=0):
        words.append(i)

print(*words)

# Write a Python Program to print only the odd length word seperated by commas
str1=input()
list1 = str1.split(',')

words=[]

for i in list1:
    if (len(i)%2!=0):
        words.append(i)

print(*words,sep=',')

#Python program to print only the odd length words one under the other
n = int(input())
list1=[]
for i in range(n):
    list1.append(input())

odd=[]

for i in list1:
    if (len(i)%2!=0):
        odd.append(i)

print(*odd,sep='\n')