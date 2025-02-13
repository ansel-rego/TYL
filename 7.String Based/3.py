'''
Two people made a list of movies they like and dislike.
Write a Python program to find the number of movies they both like and the number of movies they both dislike.
Input Description:
Input1 and Input2 are strings containing 1s and 0s. 1s represent likes and 0s represent dislikes.
Sample Input:
101011000
011001010
Sample Output:
2,3
'''

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