'''
You are given two sentences. Write a Python program to print only the common words of the two sentences.
If there are no common words, then print "Nil".
Sample Input:
cmrit ece third sem
vtu cmrit ece
Sample Output:
cmrit ece
'''

#Code starts here:
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
#Code ends here.
