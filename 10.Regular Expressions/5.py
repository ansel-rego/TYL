'''
You are given a list of stirngs. Write a program to print only the valid URLs from the given list.
If there is no valid URL,print "Nil". 
Input Description:
First entry tells how many strings are present in the given list. Then the strings are entered one below the other.

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

#Code starts here:
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
#Code ends here.
