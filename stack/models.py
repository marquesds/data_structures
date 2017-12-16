from stack.exceptions import StackOverFlowException, StackUnderFlowException

MAX_SIZE = 40


class Element(object):
    def __init__(self, data, next_element):
        self.data = data
        self.next = next_element

    def __str__(self):
        return str(self.data)


class Stack(object):
    size = 0
    top = None

    def push(self, data):
        if self.full():
            raise StackOverFlowException()
        self.top = Element(data, self.top)
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
