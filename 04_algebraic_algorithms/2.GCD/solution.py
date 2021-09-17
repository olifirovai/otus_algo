def euclid_subtracting(data: list) -> int:
    a = data[0]
    b = data[1]
    while a != b:
        while a > b:
            a -= b
        while b > a:
            b -= a
    return a


def euclid_division(data: list) -> int:
    a = data[0]
    b = data[1]
    max_value = max(a, b)
    min_value = min(a, b)
    while max_value != 0 and min_value != 0:
        if max_value % min_value == 0:
            return min_value
        else:
            max_value, min_value = max_value % min_value, max_value


def steinitz_algorithm(data: list) -> int:
    pass
