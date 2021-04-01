class MyQueue:
    def __init__(self):
        self.rear = -1
        self.front = -1
        self.N = 10
        self.lst = [0]*self.N
    # enQueue(value) : Queue 에 요소를 넣는 기능
    def enQueue(self, value):
        self.rear += 1
        self.lst[self.rear] = value
    # deQueue() : Queue 의 front를 반환하고 삭제하는 기능
    def deQueue(self):
        self.front += 1
        return self.lst[self.front]
    # isEmpty() : Queue 가 비어있는지 확인하는 기능
    def isEmpty(self):
        if self.front == self.rear:
            return True
        return False
    # isFull() : Queue 가 가득 찼는지 확인하는 기능
    def isFull(self):
        if self.rear == self.N-1:
            return True
        return False
    # Qpeek() : Queue의 front를 반환
    def Qpeek(self):
        return self.lst[self.front+1]
