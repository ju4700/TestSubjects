# 36. Map two lists to a dictionary
def lists_to_dict(keys, values):
    return dict(zip(keys, values))

# 37. Implementing a stack using a list
class Stack:
    def _init_(self):
        self.stack = []
     
    def push(self, item):
        self.stack.append(item)

    def pop(self):
        return self.stack.pop() if self.stack else None

# 38. Implementing a queue using a list
class Queue:
    def _init_(self):
        self.queue = []
     
    def enqueue(self, item):
        self.queue.append(item)
     
    def dequeue(self):
        return self.queue.pop(0) if self.queue else None