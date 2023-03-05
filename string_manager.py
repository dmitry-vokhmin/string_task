from string import BaseString


class StringManager:
    def __init__(self, string: BaseString):
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
