'''
Write a Python program to convert Roman number into equivalent decimal number.
(Roman Numbers: I->1,V->5,X->10,L-.50,C->100,D->500,M->1000)
Sample Input:
IX
Sample Output:
9
'''

str1=input()
rom={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
dec=0
for i in range(len(str1)):
    present=rom[str1[i]]
    past=rom[str1[i-1]]
    if present>past and i!=0:
        dec=dec+present-2*past
    else:
        dec=dec+present
print(dec)