'''
Write a program to take dates as string input and convert dates of yyyy-mm-dd format to dd-mm-yy format.
If the date is in dd-mm-yyyy format do not change it.
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
