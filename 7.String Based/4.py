'''
Write a Python program to compute the net amount of a bank account based on a transaction log.
Input Description:
The input transaction log is as follows:
First Line: Integer n, which specifies the names of transactions.
Second line onwards: A character and an integer seperated by space.
Character D indicates deposit(D) and Character W indicates withdrawal(W).
The integer part indicates the amount.
Output Description:
For Ex.
B 500
which indicates a balance of 500 Rs.
Sample Input:
4
D 500
D 1000
W 200
W 300
Sample Output:
B 1000
'''

#Code starts here:
n=int(input())
list1=[]
for i in range(n):
    list1.append(input())
bal=0
for i in list1:
    if i[0]=='D':
        bal=bal+int(i[2:])
    elif i[0]=='W':
        bal=bal-int(i[2:])
print('B',bal)
#Code ends here.
