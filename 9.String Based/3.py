'''
Voting was held in a class to elect class representative.
A list of names students voted is given to you. Write a Python program to find who got the maximum number of votes. 
If two students got equal number of votes, then elect the one whose name comes first in alphabetical order.
Also display the number of votes the winner got.
Sample Input:
raveesh mahesh raveesh mahesh rajesh rakesh rajesh rakesh raveesh mahesh
Sample Output:
mahesh,3
'''

#Code starts here:
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
#Code ends here.
