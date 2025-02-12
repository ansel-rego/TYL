'''
You are given 2 strings.Write a Python program to print the similarity value of the two.
Similarity value=(2*Number of ame positions)/Total number of letters.
Print the value for 3 decimal places.
Sample Input:
cmrit
crmi
Sample Output:
0.444
'''

str1=input()
str2=input()
total=len(str1)+len(str2)
m=min(len(str1),len(str2))
similar=0
for i in range(m):
    if str1[i]==str2[i]:
        similar+=1
similarity_value=(2*similar)/total
print('%0.3f'%similarity_value)
