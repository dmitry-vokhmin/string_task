from enum import StrEnum

from string.base import BaseString


class StringType(StrEnum):
    string = 'string'
    hash_string = 'hash_string'


class HashString(BaseString):
    def __init__(self, chars: str = ''):
        self._chars = chars
        self._hash = hash(chars)

    def clear(self):
        self._chars = ''
        self._hash = None

    def __len__(self):
        return len(self._chars)

    def __add__(self, other: str):
        self._chars += other
        self._hash = hash(self._chars)
        return self._chars

    def __iadd__(self, other: str):
        self._chars += other
        self._hash = hash(self._chars)
        return self._chars

    def __str__(self):
        return str(self._hash)

    def __getitem__(self, idx: int):
        return self._chars[idx]


class String(BaseString):
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
