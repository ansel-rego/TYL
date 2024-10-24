#You are given a list of unique names.Write a Python program to print the names that start with "R" or "r" and end with "H" or "h".If there are no such names, print -1.
str1=input()
list1=str1.split(',')
list2=[]
for i in list1:
    if i[0]=='R' or i[0]=='r':
        if i[-1]=='H' or i[-1]=='h':
            list2.append(i)   

if (len(list2)==0):
    print(-1)
else:
    print(*list2,sep='\n')


#You are given a list of words. Write a Python program to print only the palindromes present in the list.If there are no palindromes in the given list,then print "Nil"
n=int(input())
list1=[]
list2=[]
for i in range (0,n):
    list1.append(input())
for i in list1:
    if i==i[::-1]:
        list2.append(i)
if len(list2)==0:
    print('Nil')
else:
    print(*list2,sep='\n')


#Two people made a list of movies they like and dislike.
#Write a Python program to find the number of movies they both like and the number of movies they both dislike.
str1=input()
str2=input()
likes=0
dislikes=0
for i in range(len(str1)):
    if str1[i]=='1' and str2[i]=='1':
        likes+=1
    elif str1[i]=='0' and str2[i]=='0':
        dislikes+=1
print(likes,dislikes,sep=',')


#Write a Python program to compute the net amount of a bank account based on a transaction log.
#The input transaction log is as follows: Integer n, which specifies the namer of transactions.
#Second line onwards: A character and an integer seperated by space.
#Character D indicates deposit(D) and Character W indicates withdrawal(W).
#The integer part indicates the amount.
n=int(input())
list1=[]
for i in range(n):
    list1.append(input())
bal=0
for i in list1:
    if i[0]=='D':
        bal=bal+int(i[2:])
    elif i[0]=='W':
        bal=bal-int(i[2:])
print('B',bal)


#Given a string, write a Python program to remove all the spaces and find their length.
#Also, output whether the length is even or odd
str1=input()
str2=str1.split()
str3=''.join(str2)
if len(str3)%2==0:
    print(len(str3),'even')
else:
    print(len(str3),'odd')

#You are given two sentences. Write a Python program to print only the common words of the two sentences.
#If there are no common words, then print "Nil".
str1=input()
str2=input()
list1=str1.split()
list2=str2.split()
list3=[]
for i in list1:
    if i in list2:
        list3.append(i)
if len(list3)!=0:
    print(*list3)
else:
    print('Nil')


#You are given a sentence. Write a Python program to remove the repeated words of length greater than 5.
str1=input()
list1=str1.split()
list2=[]
for i in list1:
    if (i in list2 and len(i)>5):
        continue
    else:
        list2.append(i)
print(*list2)


#You are given a sentence. Write a Python program to remove the non-repeated words of length greater than 5



#You are given a sentence. Write a Python program to extract only the odd length words. If the length of those words is less than 10.
#The pad them with * in the right and make their length 10.
#If the off length word has greater than 10 letters,print the word as it is
str1=input()
list1=str1.split()

for i in list1:
    if len(i)%2!=0:
        if len(i)<10:
            i=i+('*'*(10-len(i)))
            print(i)