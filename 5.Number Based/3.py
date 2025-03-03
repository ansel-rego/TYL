'''
Write a Python program that takes a list of numbers and prints only those numbers which are not repeated.If there are non-repeated numbers,print "None".
Input Description:
First Input tells the number of elements. Then elements are entered one below the other.
Sample Input:
6
1
2
3
3
2
4
Sample Output:
1
4
'''

#Code starts here:
n=int(input())
list1=[]
list2=[]
for i in range(n):
    list1.append(int(input()))
for i in list1:
    if list1.count(i)==1:
        list2.append(i)
if len(list2)==0:
    print("None")
else:
    print(*list2,sep='\n')
#Code ends here.
