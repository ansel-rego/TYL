'''
Write a Python program to create a class called 'Rectangle'.Include methods to calculate area of a rectange and the lenght of the diagonal.
Take the length of the sides as input from the user.
Use round(x,2) function to limit the decimal value to 2 positions.
Sample Input:
2,3
Sample Output:
6
3.61
'''
class rectangle():
    def __init__(self,l,b):
        self.length=l
        self.breadth=b
    def area(self):
        A=self.length*self.breadth
        return round(A,2)
    def diagonal(self):
        D=(((self.length)**2)+((self.breadth)**2))**0.5
        return round(D,2)

s=input()
list1=s.split(',')
rect=rectangle(int(list1[0]),int(list1[1]))

print(rect.area())
print(rect.diagonal())
