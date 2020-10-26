# Stack: A stack.
# Your implementation should pass the tests in stack.py.
# YOUR NAME

class Stack:

    def __init__(self):
        pass

    def is_empty(self):
        return self

    def pop(self):
        if self.is_empty:
            raise IndexError()

    def peek(self):
        if self.is_empty:
            raise IndexError()