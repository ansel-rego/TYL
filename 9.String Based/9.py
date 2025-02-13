'''
You are given a string containing a letters,digits and special characters.
Write a program to find the largest even numbers which can be formed from the available digits.If the number cannot be formed, then print 'Nil'
Sample Input:
cmrit@1234
Sample Output:
4312
'''

str1 = input()  # Input string containing letters, digits, and special characters
l1 = []

# Collect digits from the input
for i in str1:
    if i.isdigit():
        l1.append(int(i))

# Sort digits in descending order
l1 = sorted(l1, reverse=True)

# Try to find the largest even digit
for i in range(1, len(l1) + 1):
    if l1[-i] % 2 == 0:
        even_digit = l1[-i]
        l1.remove(even_digit)  # Remove the even digit from its position
        l1.append(even_digit)  # Append it to the end
        break
else:
    # If no even digit is found, print 'Nil'
    print('Nil')
    exit()

# Form the number from the digits
n = ''.join(map(str, l1))

# Check if the number is even and print the result
if int(n) % 2 == 0:
    print(n)
else:
    print('Nil')