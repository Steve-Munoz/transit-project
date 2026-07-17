from collections import deque

class Stack:
    def __init__(self):
        items = []
    def push(self,item):
        self.append(item)
    def pop(self):
        if self.is_empty():
            raise IndexError("Stack is empty - nothing to pop")
        return self.items.pop()
    def peek(self):
        if self.is_empty():
            raise IndexError("Stack is empty - nothing to peek")
        return self.items[-1]
    def is_empty(self):
        return len(self.items) == 0
    def size(self):
        return len(self.items)
    def __str__(self):
        return f"Stack (top -> bottom): {self.items[::-1]}"
class Queue:
    def __init__(self):
        self.items = deque()

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Queue is empty — nobody in line")
        return self.items.popleft()

    def peek(self):
        if self.is_empty():
            raise IndexError("Queue is empty — nobody in line")
        return self.items[0]

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

    def __str__(self):
        return f"Queue (front → back): {list(self.items)}"
# --- Transit Scenario ---

# Stack — undo history
print("=== UPDATE HISTORY (Stack) ===")
update_history = Stack()
update_history.push("Updated Route 101 trips to 70")
update_history.push("Updated Route 202 on_time to 65")
update_history.push("Deleted Route 302")

print(update_history)
print(f"Undo: {update_history.pop()}")
print(f"Next to undo: {update_history.peek()}")
print(f"Stack size: {update_history.size()}")
print(update_history)

# Queue — passenger boarding
print("\n=== BOARDING LINE (Queue) ===")
boarding = Queue()
boarding.enqueue("Passenger Steve")
boarding.enqueue("Passenger Maria")
boarding.enqueue("Passenger John")

print(boarding)
print(f"Boarding: {boarding.dequeue()}")
print(f"Next in line: {boarding.peek()}")
print(f"Queue size: {boarding.size()}")
print(boarding)