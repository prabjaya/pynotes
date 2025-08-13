class Stack:
    def __init__(self):
        self.Stack = []

    def push(self,item):
        self.Stack.append(item)
    
    def size(self):
        return len(self.Stack)

    def display(self):
        print("Stack",self.Stack)

s = Stack()
s.push(10)
s.push(20)
s.push(30)
s.display()

print(s.size())

# Stack Program using Custom Functions

# # Initialize an empty stack
# stack = []

# # Function to push an element onto the stack
# def push(stack, item):
#     stack.append(item)
#     print(f"Pushed {item} onto the stack")

# # Function to pop an element from the stack
# def pop(stack):
#     if is_empty(stack):
#         return "Stack is empty"
#     return stack.pop()

# # Function to get the top element without removing it
# def peek(stack):
#     if is_empty(stack):
#         return "Stack is empty"
#     return stack[-1]

# # Function to check if the stack is empty
# def is_empty(stack):
#     return len(stack) == 0

# # Function to get the size of the stack
# def size(stack):
#     return len(stack)

# # Function to display the stack
# def display(stack):
#     print("Stack:", stack)


# # Example Usage
# push(stack, 10)
# push(stack, 20)
# push(stack, 30)
# display(stack)  # Output: Stack: [10, 20, 30]

# print("Popped:", pop(stack))  # Output: Popped: 30
# print("Top Element:", peek(stack))  # Output: Top Element: 20
# print("Is Stack Empty?", is_empty(stack))  # Output: False
# print("Stack Size:", size(stack))  # Output: 2








