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