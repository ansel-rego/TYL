'''
Write a Python program that takes an integer as input and forms a new number which has the least significant digit of the original number in its one's place and totoal number of digits of the original number in its ten's place.
Sample Input:
247
Sample Output:
37
'''

n=int(input())
l=len(str(n))
m=n%10
new=str(l)+str(m)
print(new)