from string import BaseString
from string_manager import StringManager


class Stack:
    def __init__(self, elem: BaseString | StringManager):
        self._stack = [elem]

    def append(self, item: BaseString | StringManager):
        self._stack.append(item)

    def delete(self):
        self._stack = self._stack[:-1]

    def show(self):
        return [str(elem) for elem in self._stack]

    @property
    def top_element(self):
        return self._stack[-1]

    @property
    def empty(self):
        return 0 if len(self._stack) else 1
