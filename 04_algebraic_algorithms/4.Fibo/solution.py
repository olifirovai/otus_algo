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


def fib_matrix(number: int) -> int:
    pass
