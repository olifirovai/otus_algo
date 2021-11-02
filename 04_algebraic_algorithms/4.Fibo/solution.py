from decimal import (Decimal, ROUND_FLOOR, InvalidOperation, Overflow)


def fib_recursive(number: int) -> int:
    if number < 2:
        return number
    return fib_recursive(number - 1) + fib_recursive(number - 2)


def golden_ratio(number: int) -> int:
    if number < 2:
        return number
    try:
        sqrt_5 = Decimal(5).sqrt()
        fib = Decimal(1 + sqrt_5) / Decimal(2)
        fibonacci = fib ** Decimal(number) / sqrt_5 + Decimal(1 / 2)
        fibonacci = float(
            Decimal(fibonacci).quantize(Decimal("1."), rounding=ROUND_FLOOR))
        return int(fibonacci)
    except (InvalidOperation, Overflow):
        pass


def fib_iteration(number: int) -> int:
    fib_num = 0
    if number < 2:
        fib_num = number
        return fib_num

    i, first_number, second_number = 1, 1, 1

    while i < number:
        if i <= 1:
            fib_num = i
        else:
            fib_num = first_number + second_number
            first_number = second_number
            second_number = fib_num
        i = i + 1
    return fib_num


def multiply(matrix_a, matrix_b):
    matrix_c = []
    n = len(matrix_a)
    for i in range(n):
        list_1 = []
        for j in range(n):
            val = 0
            for k in range(n):
                val = val + matrix_a[i][k] * matrix_b[k][j]
            list_1.append(val)
        matrix_c.append(list_1)
    return matrix_c


def fib_matrix(number: int) -> int:
    if number == 0 or number == 1:
        return number

    res_matrix = [[1, 0], [0, 1]]
    fibonacci_matrix = [[1, 1], [1, 0]]
    pwr = number - 1
    while pwr > 0:
        if pwr % 2 == 1:
            res_matrix = multiply(res_matrix, fibonacci_matrix)
        fibonacci_matrix = multiply(fibonacci_matrix, fibonacci_matrix)
        pwr //= 2

    return res_matrix[0][0]
