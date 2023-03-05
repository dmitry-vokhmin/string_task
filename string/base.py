from abc import ABC, abstractmethod


class BaseString(ABC):
    @abstractmethod
    def clear(self):
        pass

    @abstractmethod
    def __len__(self):
        pass

    @abstractmethod
    def __add__(self, other: str):
        pass

    @abstractmethod
    def __iadd__(self, other: str):
        pass

    @abstractmethod
    def __str__(self):
        pass

    @abstractmethod
    def __getitem__(self, idx: int):
        pass
