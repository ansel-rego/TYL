'''
Write a Python program to implement a class 'Stack'
Include methods to 
1. push an element (insert an element in the topmost position)
2. pop an element (delete the topmost element and return it)
3. peek (return the topmost element)
4. check the size of the stack (return the length)
5. check whether the stack is empty or not (return True or False)
Sample Input:
2,4,6,8
Sample Output:
8
6
3
False
'''
class Stack:
    def __init__(self):
        self.stack = []

    def push(self, element):
        self.stack.append(element)

    def pop(self):
        if self.is_empty():
            raise IndexError("pop from empty stack")
        return self.stack.pop()

    def peek(self):
        if self.is_empty():
            raise IndexError("peek from empty stack")
        return self.stack[-1]

    def size(self):
        return len(self.stack)

    def is_empty(self):
        return len(self.stack) == 0

str1=input()
list1=str1.split(',')


if __name__ == "__main__":
    s = Stack()
    
    for element in [list1[0],list1[0],list1[0],list1[0]]:
        s.push(element)
    print(s.peek())    
    print(s.pop())     
    print(s.size())    
    print(s.is_empty())  



'''
You are given a list of strings containing letters, (, ),{, },[, ]. Write a Python program to print the strings in which parenthesis are matched.
Input Description:
First integer represents the length of the list.
Then the list elements are entered one below the other.
Sample Input:
4
[ra(vee{s}h)]
ra(vee{s}h)]
]ra(vee{s}h)[
[ra{vee(s)h}]
Sample Output:
[ra(vee{s}h)]
[ra{vee(s)h}]
'''
def is_matched(string):
    stack = []
    mapping = {')': '(', '}': '{', ']': '['}
    
    for char in string:
        if char in "({[":
            stack.append(char)
        elif char in ")}]":
            if not stack or stack[-1] != mapping[char]:
                return False
            stack.pop()
    return len(stack) == 0

def filter_matched_parentheses(strings):
    return [string for string in strings if is_matched(string)]


if __name__ == "__main__":
    n = int(input())  
    strings = [input().strip() for _ in range(n)]
    
    matched_strings = filter_matched_parentheses(strings)
    for matched in matched_strings:
        print(matched)
