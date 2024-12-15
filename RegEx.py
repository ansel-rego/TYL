'''You are given a list of strings. Write a Python program to output only valid USNs from the given list. If there are no valid USNs, then print 'Nil'.
A valid USN contains exactly 10 characters out of them 1st character is a digit, the next 2 characters are alphabetical characters, then two digits, then 2 alphabetical characters, then 3 digits.
Sample INPUT:
4
1CR22EC285
CR22EC285
1CR22EC2894
1CR22EC286

Sample OUTPUT:
1CR22EC285
1CR22EC286
'''

#without using RegEx:
n=int(input())
list1=[]
list2=[]

for i in range(n):
    list1.append(input())

for i in list1:
    if len(i)==10 and i[0].isdigit() and i[1:3].isalpha() and i[3:5].isdigit() and i[5:7].isalpha() and i[7:].isdigit():
        list2.append(i)

if len(list2)!=0:
    print(*list2,sep='\n')
else:
    print('Nil')


#using RegEx:
import re
n=int(input())
list1=[]
list2=[]
for i in range(n):
    list1.append(input())

sp=re.compile('^(\d){1}[A-Z]{2}(\d){2}[A-Z]{2}(\d){3}$')

for i in list1:
    if sp.search(i):
        list2.append(i)

if len(list2)!=0:
    print(*list2,sep='\n')
else:
    print('Nil')


'''You are given a list of strings. Write a Python program to print only the valid PAN(Permanent Acoount Number) from the given list. If there are no valid PANs, then print 'Nil'.
A PAN contains 5 letters followed by 4 digits followed by 1 letter.
Input Description:
The first entry tells the number of strings.Then the strings are entered one below the other.

Sample INPUT:
4
BDDCH6708X
BDDCH6708
BDCH6708X
XVVFG9807T

Sample OUTPUT:
BDDCH6708X
XVVFG9807T
'''

#without using RegEx:
n = int(input())
list1=[]
for i in range(n):
    list1.append(input())

list2=[]
for i in list1:
    if len(i)==10 and i[0:5].isalpha() and i[5:9].isdigit() and i[-1].isalpha():
        list2.append(i)

if len(list2)!=0:
    print(*list2,sep='\n')
else:
    print('Nil')


#using RegEx:
import re
n = int(input())
list1=[]
list2=[]
for i in range(n):
    list1.append(input())

sp=re.compile('^[A-Z]{5}(\d){4}[A-Z]{1}$')

for i in list1:
    if sp.search(i):
        list2.append(i)

if len(list2)!=0:
    print(*list2,sep='\n')
else:
    print('Nil')


'''You are given a list of strings. Write a Python program to print only valid Vehicle Numbers from the list. If there are no valid Vehicle Numbers, then print 'Nil'.
A valid vehicle number contains 2 letters followed by 2 digits followed by two letters and then 4 digits
Input Description:
First Input tells the number of strings. Then the list elements are entred one below the other.

Sample INPUT:
4
KA63HJ2024
KA63HJ202
A63HJ2024
KA63HJ2032

Sample OUTPUT:
KA63HJ2024
KA63HJ2032
'''

import re
n = int(input())
list1=[]
list2=[]
for i in range(n):
    list1.append(input())

sp=re.compile('^[A-Z]{2}(\d){2}[A-Z]{2}(\d){4}$')

for i in list1:
    if sp.search(i):
        list2.append(i)

if len(list2)!=0:
    print(*list2,sep='\n')
else:
    print('Nil')


'''
You are given a sentence. Write a program to extract the valid phone numbers present in the sentence. If there is no valid phone number, then print 'Nil'.
For Ex. 080-2847-4463 is a valid phone number
Sample INPUT:
CMRIT Bengaluru's ECE Dept's phone number is 080-2847-4463

Sample OUTPUT:
080-2847-4463
'''
str1=input()
import re
list1=str1.split()
list2=[]
sp=re.compile('^(\d){3}\-(\d){4}\-(\d){4}$')

for i in list1:
    if sp.search(i):
        list2.append(i)

if len(list2)!=0:
    print(*list2)
else:
    print('Nil')



'''
You are given a list of stirngs. Write a program to print only the valid URLs from the given list.
If there is no valid URL,print "Nil". 
Input Description: Frist entry tells how many strings are present in the given list. Then the strings are entered one below the other.

Sample Input:
6
https://www.yahoo.com
http://blog.hubspot.com
https://www.karnatakajobs.com
abc:\\www.india.com
https://www.cmrit.ac.in
ftp://internet.address.edu

Sample Output:
https://www.yahoo.com
http://blog.hubspot.com
https://www.karnatakajobs.com
https://www.cmrit.ac.in
ftp://internet.address.edu
'''
n = int(input())
list1=[]
list2=[]
for i in range(n):
    list1.append(input())

import re
sp=re.compile('^(http|https|ftp)://([a-z])+(\.)([a-z])+(\.)([a-z]){2,3}(\.)?(([a-z]){2,3})?$') 
#sp=re.compile('^(https?|ftp):\/\/([a-zA-Z0-9_-]+(\.[a-zA-Z0-9_-]+)+)(:\d+)?(\/[^\s]*)?(\?[^\s]*)?(#[^\s]*)?$')
for i in list1:
    if sp.search(i):
        list2.append(i)

if len(list2)!=0:
    print(*list2,sep='\n')
else:
    print('Nil')




'''
You are given a sentence. Write a program to extract the valid phone numbers present in the sentence. If there is no valid phone number, then print 'Nil'.
For Ex. 080-2847-4463 is a valid phone number
Sample INPUT:
CMRIT's mobile number is +91-9078912345

Sample OUTPUT:
+91-9078912345
'''
str1=input()
import re
list1=str1.split()
list2=[]
sp=re.compile('^\+(\d){2}\-(\d){10}$')

for i in list1:
    if sp.search(i):
        list2.append(i)

if len(list2)!=0:
    print(*list2)
else:
    print('Nil')



'''
You are given a sentence.Write a program to print valid email IDs present in the sentence.
If there are no email IDs, then print "Nil"
Sample Input:
My email ID is sachin.t@gmail.com and my friend's email ID is virat_k@cmrit.ac.in
Sample Output:
sachin.t@gmail.com
virat_k@cmrit.ac.in
'''

str1=input()
list1=str1.split()
list2=[]
import re 

sp=re.compile('^([a-zA-Z0-9._%-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,})$')
for i in list1:
    if sp.search(i):
        list2.append(i)

if len(list2)!=0:
    print(*list2,sep='\n')
else:
    print('Nil')

'''
Write a program to take dates as string input and convert dates of yyyy-mm-dd format to dd-mm-yy format.
If the date is in dd-mm-yyyy format do not change.
Sample INPUT:
2016-01-20 2020-05-25 12-10-2008 01-12-2007
Sample OUTPUT:
20-01-2016 25-05-2020 12-10-2008 01-12-2007
'''
import re
str1=input()
list1=str1.split()
sp=re.compile('^(\d){2}-(\d){2}-(\d){4}$')
list2=[]
for i in list1:
    if sp.search(i):
        list2.append(i)

    else:
        str2=i[8:]+'-'+i[5:7]+'-'+i[0:4]
        list2.append(str2)

print(*list2)


'''
You are given a list of strings.Write a Python program to print only the valid IP addresses from the list.
A valid IP address contains four numbers ranging from 0 ti 255 seperated by a dot.
A number cannot start with 0 unless 0 is the only digit in that number.
if there are no valid IP addresses in the list,print "Nil".
Input Description:
Frist integer tells the number of elements in the list.
Then the elements are enetered one below the other
Sample INPUT:
4
192.168.0.1
292.168.0.1
192.168.02.1
192.16.0.1
Sample OUTPUT:
192.168.0.1
192.16.0.1
'''

