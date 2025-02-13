'''
Write a python program to create a class called 'Complex'.Each Complex object should have real part and imaginary part.
Include method to add two complex numbers.
Input Description:
First line contains real part and imaginary part of the first complex number.
Second line contains real part and imaginary part of the second complex number.
Sample Input:
2,4
1,3
Sample Output:
3 7
'''
class Complex:
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def add(self, other):
        return Complex(self.real+other.real, self.imaginary+other.imaginary)


# Input handling
if __name__ == "__main__":
    r1, i1 = map(int, input().split(','))
    r2, i2 = map(int, input().split(','))
    
    # Create Complex objects and add them
    result = Complex(r1, i1).add(Complex(r2, i2))
    
    # Print the result
    print(result.real, result.imaginary)

