#You are given a string.Write a Python program to print the number of alphabetical characters,digits,spaces,special characters.
str1=input()
alphabet=0
digits=0
spaces=0
specialchar=0
for i in str1:
    if i.isalpha():
        alphabet+=1
    elif i.isdigit():
        digits+=1
    elif i.isspace():
        spaces+=1
    else:
        specialchar+=1
print(alphabet,digits,spaces,specialchar,sep=',')


#You are given a string. Write a Python program to find the number of vowels and consenants present in the string.
str1=input()
counter_c=0
counter_v=0
for i in str1:
    if i.isalpha():
        if i in 'AEIOUaeiou':
            counter_v+=1
        else:
            counter_c+=1
print(counter_v,counter_c,sep=',')

#Your are give a string. Write a Python Program to print the number of uppercase and lowercase letters
str1=input()
counter_upper=0
counter_lower=0
for i in str1:
    if i.isupper():
        counter_upper+=1
    elif i.islower():
        counter_lower+=1
print(counter_upper,counter_lower,sep=',')

#You are given a list of strings.Write a program to remove vowels from every string and print the new list
#First entry is the number of elements in the list.Then elements are enetered one below the other 
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


#You are given a list of words.Write a Python Program to print the word with highest number of vowels in it.
#If two words have equal number of vowels, then select the word which appears first in the given list.
n=int(input())
list1=[]
for i in range(n):
    list1.append(input())
count_past=0
for i in list1:
    count_present=0
    for j in i:
        if j in 'AEIOUaeiou':
            count_present+=1
    if count_present>count_past:
        req_word=i
        count_past=count_present
print(req_word)


#You are given a list of strings. Write a Python program to print only the valid password among them.
'''A valid password contains at least:
1.2 lower case letters
2.2 upper case letters
3.at least one digit
4.no spaces
5.one special character from !@#$%^&*
Minimum word length of password is 8 and maximum length is 16'''
#First entry is an intger which gives the number of elements in the list.Then the elements of the list are entered one below the other 
n=int(input())
list1=[]
for i in range(n):
    list1.append(input())

def pw(str1):
    if len(str1)<8 or len(str1)>16:
        return False
    else:
        c_lower=0
        c_upper=0
        c_digit=0
        c_space=0
        c_character=0
        for i in str1:
            if i.isupper():
                c_upper+=1
            elif i.islower():
                c_lower+=1
            elif i.isdigit():
                c_digit+=1
            elif i.isspace():
                c_space+=1
            else:
                c_character+=1
                c_upper+=1
        if c_lower>=2 and c_upper>=2 and c_digit>=1 and c_space==0 and c_character>=1:
            return True 
        else:
            return False

list2=[]
for i in list1:
    if pw(i)==True:
        list2.append(i)

print(*list2,sep='\n')


#You are given a string. Write a program to print only the anagrams present in the string
#Anagrams means words containing same letters
str1=input()
list1=str1.split()
list2=[]
for i in range((len(list1))-1):
    if sorted(list1[i])==sorted(list1[i+1]):
        if list1[i] not in list2:
            list2.append(list1[i])
        if list1[i+1] not in list2:
            list2.append(list1[i+1])
print(*list2)


#Write a Python program to check whether a given string is Heterogram or not.
#Return True if the given string is a Histogram. Otherwise, return False
#A hetrogram is a word,phrase, or sentence in which no letter of the alphabet occurs more than once 
str1=input()
a=0
for i in str1:
    if i!=' ' and str1.count(i)>1:
        a=1
        break
if a==0:
    print(True)
else:
    print(False)

