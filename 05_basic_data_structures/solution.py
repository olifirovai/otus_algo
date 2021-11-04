from dynamic_array import DynamicArray


class SingleArray(DynamicArray):
    __slots__ = ('array',)

    def __init__(self):
        self.array = []

    def __getitem__(self, index: int):
        if index < 0 or index >= self.size():
            return IndexError(f'{index} is out of bounds')
        return self.array[index]

    def size(self) -> int:
        return len(self.array)

    def is_empty(self) -> bool:
        return self.size() == 0

    def put(self, item) -> None:
        self._resize()
        self.array[self.size() - 1] = item

    def put_at(self, item, index) -> None:
        if index <= 0:
            self.put(item)
            self.array = self.array[-1:] + self.array[:-1]

        elif index >= self.size():
            self.put(item)

        else:
            self.put(item)
            self.array = self.array[:index] + self.array[- 1:] + self.array[
                                                                 index:-1]

    def delete(self):
        if self.is_empty():
            return None
        item = self.array[self.size() - 1]
        self.array = self.array[:-1]

        return item

    def delete_at(self, index: int):
        if self.is_empty():
            return None
        if index < 0 or index >= self.size():
            return IndexError(f'{index} is out of bounds')
        elif index == self.size() - 1:
            return self.delete()
        else:
            item = self.array[index]
            self.array = self.array[:index] + self.array[index + 1:]

            return item

    def _resize(self) -> None:
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
        if index >= self.cur_size or index < 0:
            return IndexError(f'{index} is out of bounds')
        return self.array[index]

    def size(self) -> int:
        return self.cur_size

    def is_empty(self) -> bool:
        return self.size() == 0

    def put(self, item) -> None:
        if self.size() == len(self.array):
            self._resize()
        self.array[self.size()] = item
        self.cur_size += 1

    def put_at(self, item, index) -> None:
        if index >= self.size():
            self.put(item)
        elif index <= 0:
            self.put(item)
            self.array = self.array[-1:] + self.array[:-1]
        else:
            self.put(item)
            self.array = self.array[:index] + self.array[- 1:] + self.array[
                                                                 index:-1]

    def delete(self):
        if self.is_empty():
            return None
        item = self.array[self.cur_size - 1]
        self.array[self.cur_size - 1] = None
        self.cur_size -= 1

        return item

    def delete_at(self, index: int):
        if index >= self.cur_size or index < 0:
            return IndexError(f'{index} is out of bounds')
        elif index == self.cur_size - 1:
            self.delete()
        else:
            item = self.array[index]
            self.array = self.array[:index] + self.array[index + 1:]
            self.cur_size -= 1
            return item

    def _resize(self) -> None:
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
        if index >= self.cur_size or index < 0:
            return IndexError(f'{index} is out of bounds')
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

    def put_at(self, item, index) -> None:
        if self.size() <= index:
            self.put(item)
        elif index <= 0:
            self.put(item)
            self.array = self.array[-1:] + self.array[:-1]
        else:
            self.put(item)
            self.array = self.array[:index] + self.array[- 1:] + self.array[
                                                                 index:-1]

    def delete(self):
        if self.is_empty():
            return None
        item = self.array[self.cur_size - 1]
        self.array[self.cur_size - 1] = None
        self.cur_size -= 1
        return item

    def delete_at(self, index: int):
        if self.cur_size <= index or index < 0:
            return IndexError(f'{index} is out of bounds')
        elif index == self.cur_size - 1:
            self.delete()
        else:
            item = self.array[index]
            self.array = self.array[:index] + self.array[index + 1:]
            self.cur_size -= 1
            return item

    def resize(self) -> None:
        new_array = [0] * (self.size() * 2 + 1)
        for i in range(self.size()):
            new_array[i] = self.array[i]
        self.array = new_array


class MatrixArray(DynamicArray):
    __slots__ = ('array', 'cur_size', 'rows', 'columns')

    def __init__(self):
        self.cur_size = 0
        self.rows = 1
        self.columns = 5
        self.array = self.make_matrix(self.rows, self.columns)

    def __getitem__(self, index: int):
        if index >= self.cur_size or index < 0:
            return IndexError(f'{index} is out of bounds')
        item = self.array[self.get_row(index)][self.get_column(index)]
        return item

    def __setitem__(self, index, value):
        # if self.cur_size <= index or index < 0:
        #     return IndexError(f'{index} is out of bounds')
        if not 0 <= index < self.cur_size:
            return IndexError(f"{index} is out of bounds!")

        row = self.get_row(index)
        col = self.get_column(index)
        self.array[row][col] = value

    def get_row(self, index):
        return index // self.columns

    def get_column(self, index):
        return index % self.columns

    def size(self) -> int:
        return self.cur_size

    def is_empty(self) -> bool:
        return self.size() == 0

    def put(self, item) -> None:
        if self.size() == self.rows * self.columns:
            self._resize()
        row = self.get_row(self.cur_size)
        column = self.get_column(self.cur_size)
        self.array[row][column] = item
        self.cur_size += 1

    def put_at(self, item, index: int) -> None:
        if index >= self.rows * self.columns:
            self.put(item)
        if index <= 0:
            index = 0
        self.put(item)
        for i in range(index, self.cur_size - 1):
            self[i], self[self.cur_size - 1] = self[self.cur_size - 1], self[i]

    def delete(self):
        if self.is_empty():
            return None
        item = self[self.cur_size - 1]
        self[self.cur_size - 1] = None
        self.cur_size -= 1

        return item

    def delete_at(self, index: int):
        if index >= self.cur_size or index < 0:
            return IndexError(f'{index} is out of bounds')
        if index == self.cur_size - 1:
            self.delete()
        item = self[index]
        for i in range(index, self.cur_size - 1):
            self[i] = self[i + 1]
        self[self.cur_size - 1] = None
        self.cur_size -= 1

        return item

    def _resize(self) -> None:
        new_row = [[0 for i in range(self.columns)] for j in range(1)]
        self.array += new_row
        self.rows += 1

    @staticmethod
    def make_matrix(rows, columns):
        return [[0 for i in range(columns)] for j in range(rows)]
