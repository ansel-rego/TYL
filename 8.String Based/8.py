'''
Write a Python program to check whether a given string is Heterogram or not.
Return True if the given string is a Histogram. Otherwise, return False
A hetrogram is a word,phrase, or sentence in which no letter of the alphabet occurs more than once 
For Ex. 'the big dwarf only jumps'
Sample Input:
the big dwarf only jumps
Sample Output:
True
'''

#Code starts here:
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
    
#Code ends here.
