"Implementation of the stack data structure"


class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)
        return

    def pop(self):
        return self.items.pop()

    def get_stack(self):
        return self.items

    def peek(self):
        # return top most element of the stack
        if self.is_empty():
            return 'Empty'
        else:
            return self.items[-1]

    def is_empty(self):
        return self.items == []


# STACK DATA STRUCTURE QUESTIONS
# QUESTION 1 - Determine if parenthesis are balanced
balanced = '({[]})'
not_balanced = '([{(){}])'


def check_matching_parenthesis(items):
    openings = ['(', '{', '[']
    closing = [')', '}', ']']
    s = Stack()

    for item in items:
        if item in openings:
            s.push(item)
        if item in closing:
            opening = s.pop()
            if opening == '[' and item != ']' or opening == '(' and item != ')' or opening == '{' and item != '}':
                return 'imbalanced'
    if s.is_empty():
        return 'balanced'
    else:
        return 'imbalanced'


# print(check_matching_parenthesis(not_balanced))


"""
QUESTION 2 - Convert integer values to their corresponding integer values
"""


def convert_integer_to_binary(number):
    s = Stack()
    while number > 0:
        s.push(number % 2)
        number = number // 2

    binary_number = ''
    while not s.is_empty():
        binary_number += str(s.pop())

    return print(binary_number)


convert_integer_to_binary(242)
