from abc import ABCMeta, abstractmethod


class DynamicArray(metaclass=ABCMeta):

    @abstractmethod
    def __getitem__(self, index: int):
        pass

    @abstractmethod
    def size(self) -> int:
        pass

    @abstractmethod
    def is_empty(self) -> bool:
        pass

    @abstractmethod
    def put(self, item) -> None:
        pass

    @abstractmethod
    def put_at(self, item, index) -> None:
        pass

    @abstractmethod
    def delete(self) -> None:
        pass

    @abstractmethod
    def delete_at(self, index: int) -> None:
        pass
