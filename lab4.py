#Binary Search Recursive Approach
def binary_search_(arr, target, lowt, high):
    if low > high:
        return -1  #target is not found
    
    mid = low + (high - low) // 2
    
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search_recursive(arr, target, mid + 1, high)
    else:
        return binary_search_recursive(arr, target, low, mid - 1)


arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
target = 5
result = binary_search_recursive(arr, target, 0, len(arr) - 1)
print(f"Element {target} is at index {result}")



#Implement queue using python
class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Dequeue from an empty queue")
        return self.items.pop(0)

    def peek(self):
        if self.is_empty():
            raise IndexError("Peek from an empty queue")
        return self.items[0]

    def size(self):
        return len(self.items)

    def __str__(self):
        return "Queue: " + str(self.items)


q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
print(q)  # Queue: [1, 2, 3]
print(q.dequeue())  # 1
print(q)  # Queue: [2, 3]
print(q.peek())  # 2
print(q.size())  # 2



# Implement stack using python
class Stack:
    def _init_(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.is_empty():
            raise IndexError("Pop from empty stack")
        return self.items.pop()

    def peek(self):
        if self.is_empty():
            raise IndexError("Peek from empty stack")
        return self.items[-1]

    def size(self):
        return len(self.items)

    def _str_(self):
        return str(self.items)


stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
print("Stack:", stack)
print("Pop:", stack.pop())
print("Peek:", stack.peek())
print(" Stack Is empty:", stack.is_empty())
print("Stack Size:", stack.size())
