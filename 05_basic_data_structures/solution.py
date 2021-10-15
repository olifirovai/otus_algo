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
        self.array[self.cur_size - 1] = 0
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
        self.array[self.cur_size - 1] = 0
        self.cur_size -= 1
        return item

    def delete_at(self, index: int) -> None:
        if index >= self.cur_size or index < 0:
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
        self.columns = 1000
        self.array = self.make_matrix(self.rows, self.columns)

    def __getitem__(self, index: int):
        if index >= self.cur_size or index < 0:
            return IndexError(f'{index} is out of bounds')
        item = self.array[self.get_row(index)][self.get_column(index)]
        return item

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
        col = self.get_column(self.cur_size)
        self.array[row][col] = item
        self.cur_size += 1
    # TODO put_at - incorrect; delete_at
    def put_at(self, item, index) -> None:
        if index >= self.rows * self.columns:
            self.put(item)
        else:
            # for i in range(self.cur_size-2,index-1,-1)
            self.put(item)
            row = self.get_row(self.cur_size - 1)
            col = self.get_column(self.cur_size - 1)
            if index <= 0:
                self.array[0][0], self.array[row][col] = self.array[row][col], \
                                                         self.array[0][0]
            else:
                new_row = self.get_row(index)
                new_col = self.get_column(index)
                self.array[new_row][new_col], self.array[row][col] = \
                    self.array[row][col], self.array[new_row][new_col]

    def delete(self) -> None:
        if self.is_empty():
            return None
        row = self.get_row(self.cur_size - 1)
        col = self.get_column(self.cur_size - 1)
        item = self.array[row][col]
        self.array[row][col] = 0
        self.cur_size -= 1

        return item

    def delete_at(self, index: int) -> None:
        if index >= self.cur_size or index < 0:
            return IndexError(f'{index} is out of bounds')
        if index == self.cur_size-1:
            self.delete()
        else:
            row = self.get_row(index)
            col = self.get_column(index)
            item = self.array[row][col]
            self.array[row][col] = 0
            self.cur_size -= 1

            return item

    def _resize(self) -> None:
        new_row = [[0 for i in range(self.columns)] for j in range(1)]
        self.array += new_row
        self.rows += 1

    @staticmethod
    def make_matrix(rows, columns):
        return [[0 for i in range(columns)] for j in range(rows)]
