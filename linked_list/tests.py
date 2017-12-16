import unittest

from linked_list.exceptions import EmptyLinkedListException, NotFoundException
from linked_list.models import LinkedList


class LinkedListTestCase(unittest.TestCase):
    def setUp(self):
        self.linked_list = LinkedList()

    def test_add(self):
        elements = [1, 2, 3, 4, 5]
        for element in elements:
            self.linked_list.add(data=element)

        self.assertEqual('1', str(self.linked_list.head))

    def test_add_element_to_begin(self):
        pass

    def test_find(self):
        elements = [1, 2, 3, 4, 5]
        for element in elements:
            self.linked_list.add(data=element)

        found_value = self.linked_list.find(3)
        self.assertEqual(3, found_value)

    def test_pop(self):
        elements = [1, 2, 3, 4, 5]
        for element in elements:
            self.linked_list.add(data=element)

        found_value = self.linked_list.find(1)
        self.assertEqual(1, found_value)

        self.linked_list.pop()
        with self.assertRaises(NotFoundException):
            self.linked_list.find(1)

    def test_find_empty_list(self):
        with self.assertRaises(EmptyLinkedListException):
            self.linked_list.find(1)

    def test_find_unexistent_value(self):
        elements = [1, 2, 3, 4, 5]
        for element in elements:
            self.linked_list.add(data=element)

        with self.assertRaises(NotFoundException):
            self.linked_list.find(100)

    def test_pop_empty_list(self):
        with self.assertRaises(EmptyLinkedListException):
            self.linked_list.pop()


if __name__ == '__main__':
    test_case = LinkedListTestCase()
    test_case.run()
