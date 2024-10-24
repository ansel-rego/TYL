#You are given a list of strings.Write a ython program to print only thr wonderul strings
#A wonderful string is a string which is made up of exactly three diffeent letters.
#Print "None" if there are no wonderful strings in the given list
str1=input()
list1=str1.split()
list2=[]
for i in list1:
    if len(set(i))==3:
        list2.append(i)
if len(list2)!=0:
    print(*list2)
else:
    print('None')


#You are given a list of strings.Write a Ppython program to print only those strings which start with "Hello" and end with a digit.
#First entry tells the number of strings.The the strings are enetered one below the other 
n=int(input())
list1=[]
list2=[]
for i in range(n):
    list1.append(input())

for i in list1:
    if i.startswith("Hello") or i.endswith("0123456789"):
        list2.append(i)

print(*list2,sep='\n')


n=int(input())
list1=[]
list2=[]
for i in range(n):
    list1.append(input())

for i in list1:
    if i[0:5]=='Hello' and i[-1].isdigit():
        list2.append(i)

print(*list2,sep='\n')


#Voting was held in a class to elect class representative.
#A list of names students voted is given to you. Write a Python program to find who got the maximum number of votes. 
#If two students got equal number of votes, then elect the one whose name comes first in alphabetical order.
#Also display the number of votes the winner got.
#input: raveesh mahesh raveesh mahesh rajesh rakesh rajesh rakesh raveesh mahesh
#output: mahesh,3
str1=input()
list1=str1.split()
dict1={}
for i in list1:
    key=i
    dict1[key]=list1.count(i)

max_votes=max(dict1.values())
for i in sorted(dict1.keys()):
    if dict1[i]==max_votes:
        winner=i
        break

print(winner,max_votes,sep=',')


#You are given several strings containing Os and 1s.
#O indicates an empty parking space and 1 indicates an occupied parking space.
#Imagine a new vehicle enters the parking lot.
#Write a Python program to allot parking space in the row which contains maximum number of empty slots.
#In case two rows have equal number of empty slots, then the program should choose the row which appears first in the list.#
#In case there are no empty space for parking, then print "None".
#Input Description: First integer represents the number of rows. Then the strings are entered one below the other.
n = int(input())
list1=[]
list2=[]
for i in range(n):
    list1.append(input())
for i in list1:
    c=i.count("0")
    list2.append(c)
m=max(list2)
if m==0:
    print('None')
else:
    for i in range(len(list2)):
        if m==list2[i]:
            print(i+1)
            break


#A car company numbers the engines based on the cars number plate.
#The engine number is the sum of all the integers present on the cars number plate.
#Develop a Python program whixh takes input in the form of a string(Car Number) and gives back the engine number in the form of an integer.
str1=input()
num=0
for i in str1:
    if i.isdigit():
        num+=int(i)
print(num)


#You are given a list of email IDs.Write a program to extract name of the employee and the name of the company
#Input description:First integer gives the number of elements.The elements are entered one below the other 
n=int(input())
list1=[]
for i in range(n):
    list1.append(input())

for i in list1:
    list2=i.split('@')
    list3=list2[1].split('.')
    print(list2[0],list3[0],sep=',')


#You are given a list of integers.Write a Python program to output a dictionary with the numbers as keys and their frequency of occurances as values.
#Arrange the dictionary elements in the ascending order of their keys.
str1=input()
list1=str1.split(',')
list1=[int(i) for i in list1]
dict1={}
for i in sorted(list1):
    key=i
    dict1[key]=list1.count(i)
print(dict1)



#Write a Python program to convert Roman number into equivalent deicmal number.
#(Romaan Numbers: I->1,V->5,X->10,L-.50,C->100,D->500,M->1000)
str1=input()
rom={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
dec=0
for i in range(len(str1)):
    present=rom[str1[i]]
    past=rom[str1[i-1]]
    if present>past and i!=0:
        dec=dec+present-2*past
    else:
        dec=dec+present
print(dec)



str1=input()
rom={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
dec=0
for i in range(len(str1)):
    present=rom[str1[i]]
    dec=dec+present

if rom[str1[-1]]>rom[str1[-2]]:
    dec=dec-2*rom[str1[-2]]

print(dec)



#You are given 2 strings.Write a Python program to print the similarity value of the two.
#Similarity value=(2*Number of ame positions)/Total number of letters.
#Print the value for 3 decimal places
str1=input()
str2=input()
total=len(str1)+len(str2)
m=min(len(str1),len(str2))
similar=0
for i in range(m):
    if str1[i]==str2[i]:
        similar+=1
similarity_value=(2*similar)/total
print('%0.3f'%similarity_value)


#You are given a string containing a letters,digits and special characters.Write a program to find the largest even numbers which can be formed from the available digits.If the number cannot be formed, then print 'Nil'