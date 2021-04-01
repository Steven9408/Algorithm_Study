class Stack:
    def __init__(self):
        self.top = -1
        self.data = []

    def push(self, val):
        self.data.append(val)
        self.top += 1

    def pop(self):
