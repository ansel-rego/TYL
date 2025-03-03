'''
Write a python program to create a class representing a circle. Include methods to calculate its area and cirumference
Take redius of the circle as input from the user.
Sample Input:
3
Sample Output:
28.274333882308138
18.84955592153876
'''

#Code starts here:
class circle:
    def __init__(self,r):
        self.radius=r
    def area(self):
        import math
        A=(math.pi)*(self.radius**2)
        return A
    def circumference(self):
        import math
        C=2*(math.pi)*self.radius
        return C

r=int(input())
c=circle(r)

print(c.area())
print(c.circumference())
#Code ends here.
