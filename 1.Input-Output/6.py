'''
You are given a list of words.
Write a python program to print only the odd length words one under the other
Input Description:
First integer tells the number of words.
Then the words are entered one below the other.
Sample Input:
4
Rohit
Virat
Hardik
Bumra
Sample Output:
Rohit
Virat
'''

#Code starts here:
n = int(input())
list1=[]
for i in range(n):
    list1.append(input())

odd=[]

for i in list1:
    if (len(i)%2!=0):
        odd.append(i)

print(*odd,sep='\n')
#Code ends here.
