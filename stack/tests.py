import unittest

from stack.exceptions import StackOverFlowException, StackUnderFlowException
from stack.models import Stack


class StackTestCase(unittest.TestCase):
    def setUp(self):
        self.stack = Stack()

    def test_push(self):
        elements = [1, 2, 3, 4, 5]
        for element in elements:
            self.stack.push(data=element)

        self.assertEqual(str(elements[len(elements) - 1]), str(self.stack.pop()))

    def test_pop(self):
        elements = [1, 2, 3, 4, 5]
        for element in elements:
            self.stack.push(data=element)

        for element in elements[::-1]:
            self.assertEqual(str(self.stack.pop()), str(element))

    def test_peek(self):
        elements = [1, 2, 3, 4, 5]
        for element in elements:
            self.stack.push(data=element)

        self.assertEqual(str(elements[len(elements) - 1]), str(self.stack.peek()))

    def test_empty(self):
        self.assertTrue(self.stack.empty())

    def test_full(self):
        elements = list(range(40))
        for element in elements:
            self.stack.push(data=element)

        self.assertTrue(self.stack.full())

    def test_push_item_full_stack(self):
        elements = list(range(40))
        for element in elements:
            self.stack.push(data=element)

        with self.assertRaises(StackOverFlowException):
            self.stack.push(100)

    def test_pop_item_empty_stack(self):
        with self.assertRaises(StackUnderFlowException):
            self.stack.pop()

    def test_peek_item_empty_stack(self):
        with self.assertRaises(StackUnderFlowException):
            self.stack.pop()


if __name__ == '__main__':
    test_case = StackTestCase()
    test_case.run()
