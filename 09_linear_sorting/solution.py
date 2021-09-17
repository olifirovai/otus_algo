def quick_sort(data: list) -> list:
    if len(data) < 2:
        return data
    else:
        # Let's pick a center index of the array
        pivot = len(data) // 2
        less, center, greater = partition(data, pivot)
        return quick_sort(less) + center + quick_sort(greater)


def partition(array: list, pivot: int):
    less = []
    center = []
    greater = []
    for i in range(len(array)):
        if array[i] < array[pivot]:
            less.append(array[i])
        elif array[i] > array[pivot]:
            greater.append(array[i])
        else:
            center.append(array[i])

    return less, center, greater


def merge_sort(data: list) -> list:
    if len(data) == 1:
        return data
    left = merge_sort(data[:len(data) // 2])
    right = merge_sort(data[len(data) // 2:])

    l, r, k = 0, 0, 0

    while l < len(left) and r < len(right):
        if left[l] <= right[r]:
            data[k] = left[l]
            l += 1
        else:
            data[k] = right[r]
            r += 1
        k += 1
    while l < len(left):
        data[k] = left[l]
        l += 1
        k += 1

    while r < len(right):
        data[k] = right[r]
        r += 1
        k += 1

    return data


def mix_merge_quick_sort(data: list) -> list:
    if len(data) < 1024:
        return quick_sort(data)

    return merge_sort(data)


def counting_sort(data: list) -> list:
    return data


def radix_sort(data: list) -> list:
    max_number = max(data)

    digit_place = 1

    lists_list = []

    for _ in range(10):
        lists_list.append([])

    while max_number / digit_place >= 1:

        for number in data:
            list_index = (number // digit_place) % 10

            lists_list[list_index].append(number)

        data.clear()

        for single_list in lists_list:
            data.extend(single_list)

            single_list.clear()

        digit_place *= 10

    return data


def bucket_sort(data: list) -> list:
    return data
