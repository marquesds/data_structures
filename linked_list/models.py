from linked_list.exceptions import EmptyLinkedListException, NotFoundException


class Node(object):
    def __init__(self, data, next_element=None):
        self.data = data
        self.next = next_element

    def __str__(self):
        return str(self.data)


class LinkedList(object):
    size = 0
    head = None

    def add(self, data):
        # Add item to the end of the list
        if not self.head:
            self.head = Node(data=data)
        else:
            current_element = self.head
            while current_element.next:
                current_element = current_element.next
            current_element.next = Node(data=data)
        self.size += 1

    def find(self, data):
        if not self.head or self.empty():
            raise EmptyLinkedListException()

        while self.head:
            if data == self.head.data:
                return data
            self.head = self.head.next if self.head else None

        raise NotFoundException('{} not found.'.format(data))

    def pop(self):
        if not self.head or self.empty():
            raise EmptyLinkedListException()

        old_value = self.head.data
        self.head = self.head.next
        self.size -= 1
        return old_value

    def empty(self):
        return self.size == 0
