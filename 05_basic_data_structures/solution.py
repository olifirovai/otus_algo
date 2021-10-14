from dynamic_array import DynamicArray


class SingleArray(DynamicArray):
    __slots__ = ('array',)

    def __init__(self):
        self.array = []

    def __getitem__(self, index: int):
        return self.array[index]

    def size(self) -> int:
        return len(self.array)

    def is_empty(self) -> bool:
        return self.size() == 0

    def put(self, item) -> None:
        self.resize()
        self.array[self.size() - 1] = item

    def put_at(self, item, index: int) -> None:
        pass

    def delete(self, index: int) -> None:
        pass

    def delete_at(self, index: int) -> None:
        pass

    def resize(self) -> None:
        new_array = [0] * (self.size() + 1)
        for i in range(self.size()):
            new_array[i] = self.array[i]
        self.array = new_array


class VectorArray(DynamicArray):
    __slots__ = ('array', 'cur_size', 'capacity')

    def __init__(self):
        self.array = []
        self.cur_size = 0
        self.capacity = 10

    def __getitem__(self, index: int):
        return self.array[index]

    def size(self) -> int:
        return self.cur_size

    def is_empty(self) -> bool:
        return self.size() == 0

    def put(self, item) -> None:
        if self.size() == len(self.array):
            self.resize()
        self.array[self.size()] = item
        self.cur_size += 1

    def put_at(self, item, index: int) -> None:
        pass

    def delete(self, index: int) -> None:
        pass

    def delete_at(self, index: int) -> None:
        pass

    def resize(self) -> None:
        new_array = [0] * (self.size() + self.capacity)
        for i in range(self.size()):
            new_array[i] = self.array[i]
        self.array = new_array


class FactorArray(DynamicArray):
    __slots__ = ('array', 'cur_size',)

    def __init__(self):
        self.array = []
        self.cur_size = 0

    def __getitem__(self, index: int):
        return self.array[index]

    def size(self) -> int:
        return self.cur_size

    def is_empty(self) -> bool:
        return self.size() == 0

    def put(self, item) -> None:
        if self.size() == len(self.array):
            self.resize()
        self.array[self.size()] = item
        self.cur_size += 1

    def put_at(self, item, index: int) -> None:
        pass

    def delete(self, index: int) -> None:
        pass

    def delete_at(self, index: int) -> None:
        pass

    def resize(self) -> None:
        new_array = [0] * (self.size() * 2 + 1)
        for i in range(self.size()):
            new_array[i] = self.array[i]
        self.array = new_array


class MatrixArray(DynamicArray):
    __slots__ = ('array', 'cur_size',)

    def __init__(self):
        self.array = []
        self.cur_size = 0

    def __getitem__(self, index: int):
        return self.array[index]

    def size(self) -> int:
        return self.cur_size

    def is_empty(self) -> bool:
        return self.size() == 0

    def put(self, item) -> None:
        pass

    def put_at(self, item, index: int) -> None:
        pass

    def delete(self, index: int) -> None:
        pass

    def delete_at(self, index: int) -> None:
        pass

    def resize(self) -> None:
        pass
