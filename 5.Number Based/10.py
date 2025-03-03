'''
Write a Python program to convert the given binary number to its equivalent decimal number.
Note: Binary number is input as a string
Sample Input:
1001
Sample Output:
9
'''

#Code starts here:
binary=input()
binary=binary[::-1] #This will reverse the string
decimal=0
for i in range(len(binary)):
    decimal = decimal + (int(binary[i])*(2**i))
print(decimal)
#Code ends here.
