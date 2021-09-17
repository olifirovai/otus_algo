
def bubble_sort(n: int, array: list) -> list:
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]

    return array


def selection_sort(n: int, array: list) -> list:
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if array[min_index] > array[j]:
                min_index = j
        array[i], array[min_index] = array[min_index], array[i]

    return array


def insertion_sort(n: int, array: list) -> list:
    for i in range(1, n):
        j = i - 1

        while j >= 0 and array[i] < array[j]:
            array[i], array[j] = array[j], array[i]
            j -= 1
            i -= 1

    return array


def shell_sort(n: int, array: list) -> list:
    return array


def heap_sort(n, array):
    for i in range(n // 2 - 1, -1, -1):
        heapify(n, i, array)

    for i in range(n - 1, 0, -1):
        array[i], array[0] = array[0], array[i]
        heapify(i, 0, array)
    return array


def heapify(n: int, root: int, array: list):
    left_child = 2 * root + 1
    right_child = 2 * root + 2
    x = root
    if left_child < n and array[left_child] > array[x]:
        x = left_child
    if right_child < n and array[right_child] > array[x]:
        x = right_child
    if x != root:
        array[root], array[x] = array[x], array[root]
        heapify(n, x, array)
