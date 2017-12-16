from stack.exceptions import StackOverFlowException, StackUnderFlowException

MAX_SIZE = 40


class Stack(object):
    size = 0

    def __init__(self, top=None, next_element=None):
        self.top = top
        self.next = next_element

    def push(self, data):
        if self.full():
            raise StackOverFlowException()
        self.top = Stack(data, self.top)
        self.size += 1

    def pop(self):
        if self.empty():
            raise StackUnderFlowException()
        old_value = self.top
        self.top = self.top.next
        self.size -= 1
        return old_value

    def peek(self):
        if self.empty():
            raise StackUnderFlowException()
        return self.top

    def empty(self):
        return self.size == 0

    def full(self):
        return self.size == MAX_SIZE

    def __str__(self):
        return str(self.top)
