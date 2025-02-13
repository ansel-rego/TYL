'''
A car company numbers the engines based on the cars number plate.
The engine number is the sum of all the integers present on the cars number plate.
Develop a Python program which takes input in the form of a string(Car Number) and gives back the engine number in the form of an integer.
Sample Input:
KA57AB2056
Sample Output:
25
'''

str1=input()
num=0
for i in str1:
    if i.isdigit():
        num+=int(i)
print(num)
