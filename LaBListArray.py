class Stack:
    def __init__(self):
        self.item = []

    def push(self, item):
        self.item.append(item)

    def pop(self):
        if len(self.item) == 0 :
            return "Stack is empty"
        else:
            return self.item.pop(-1)

    def peek(self):
        if len(self.item) == 0:
            return 0
        else:
            return self.item[-1]

    def is_empty(self):
        if len(self.item) == 0:
            return True
        else:
            return False

    def size(self):
        return len(self.item)

s = Stack()
s.push(1)
s.push(2)
s.push(3)
s.push(4)
s.push(5)
print(f"""
Size after push: {s.size()}
Top element: {s.peek()}
Pop: {s.pop()}
Pop: {s.pop()}
Pop: {s.pop()}
Pop: {s.pop()}
Pop: {s.pop()}
Is empty? {s.is_empty()}
Pop from empty: {s.peek()}""")