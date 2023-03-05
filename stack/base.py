from abc import ABC
from typing import TypeVar, Generic

T = TypeVar("T")


class BaseStack(Generic[T], ABC):
    def __init__(self, elem: T):
        self._stack = [elem]

    def append(self, item: T):
        self._stack.append(item)

    def delete(self):
        self._stack = self._stack[:-1]

    def show(self) -> list[str]:
        return [str(elem) for elem in self._stack]

    @property
    def top_element(self) -> T:
        return self._stack[-1]

    @property
    def empty(self) -> int:
        return 0 if len(self._stack) else 1
