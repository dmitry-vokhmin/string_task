class String:
    def __init__(self, chars: str = ''):
        self._chars = chars

    def clear(self):
        self._chars = ''

    def __len__(self):
        return len(self._chars)

    def __add__(self, other: str):
        self._chars += other
        return self._chars

    def __iadd__(self, other: str):
        self._chars += other
        return self._chars

    def __str__(self):
        return self._chars

    def __getitem__(self, idx: int):
        return self._chars[idx]


class StringManager:
    def __init__(self, string: String):
        self._string = string

    def append(self, char: str):
        self._string += char

    @property
    def array(self) -> list[str]:
        return [char for char in self._string]

    @property
    def string(self) -> str:
        return str(self._string)

    def __getitem__(self, key: int):
        if isinstance(key, slice):
            start, stop, step = key.indices(len(self._string))
            return ''.join([self._string[i] for i in range(start, stop, step)])
        return self._string[key]

    def __str__(self):
        return f"StringManager - {self._string}"


class Stack:
    def __init__(self, elem: String | StringManager):
        self._stack = [elem]

    def append(self, item: String | StringManager):
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


if __name__ == '__main__':
    res_string = String('1234567')
    string_manager = StringManager(res_string)
    stack = Stack(res_string)
    print('StringManager ' + '-' * 100)
    print('String - ' + string_manager.string)
    print(f'Array - {string_manager.array}')
    string_manager.append('S')
    print('Append(S) - ' + string_manager.string)
    print('Get item by index - ' + string_manager[0])
    print('Get slice - ' + string_manager[2:4])
    print('Stack ' + '-' * 100)
    print(f'Initial stack - {stack.show()}')
    stack.append(string_manager)
    print(f'Append(StringManager) - {stack.show()}')
    print(f'Top element - {stack.top_element}')
    print(f'Empty - {stack.empty}')
    stack.delete()
    print(f'Delete - {stack.show()}')
