'''
You are given a list of strings. Write a Python program to print only the valid password among them.
A valid password contains at least:
1.2 lower case letters
2.2 upper case letters
3.at least one digit
4.no spaces
5.one special character from !@#$%^&*
Minimum word length of password is 8 and maximum length is 16
Input Description:
First entry is an integer which gives the number of elements in the list.Then the elements of the list are entered one below the other.
Sample Input:
5
aaBB #$1
aaBB#$1
aaBB#$12
aaBB#$12345678910
BBaa*&1234
Sample Output:
aaBB#$12
BBaa*&1234
'''

#Code starts here:
n=int(input())
list1=[]
for i in range(n):
    list1.append(input())

def pw(str1):
    if len(str1)<8 or len(str1)>16:
        return False
    else:
        c_lower=0
        c_upper=0
        c_digit=0
        c_space=0
        c_character=0
        for i in str1:
            if i.isupper():
                c_upper+=1
            elif i.islower():
                c_lower+=1
            elif i.isdigit():
                c_digit+=1
            elif i.isspace():
                c_space+=1
            else:
                c_character+=1
                c_upper+=1
        if c_lower>=2 and c_upper>=2 and c_digit>=1 and c_space==0 and c_character>=1:
            return True 
        else:
            return False

list2=[]
for i in list1:
    if pw(i)==True:
        list2.append(i)

print(*list2,sep='\n')
#Code ends here.
