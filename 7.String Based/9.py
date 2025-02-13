'''
You are given a sentence. Write a Python program to extract only the odd length words.
If the length of those words is less than 10, then pad them with * in the right and make their length 10.
If the odd length word has greater than 10 letters,print the word as it is
Sample Input:
Hi are you going to bengaluru
Sample Output:
are*******
you*******
going*****
bengaluru*
'''

str1=input()
list1=str1.split()

for i in list1:
    if len(i)%2!=0:
        if len(i)<10:
            i=i+('*'*(10-len(i)))
            print(i)