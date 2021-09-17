def simple_power(data: list) -> float:
    number = data[0]
    power = data[1]
    if power == 0:
        return 1.0
    return round(number ** power, 11)


def power_iteration(data: list) -> float:
    number = data[0]
    power = data[1]
    if power == 0:
        return 1.0

    result = number
    for _ in range(1, int(power)):
        result *= number
    return round(result, 11)


def power_two(data: list) -> float:
    number = data[0]
    power = data[1]
    if power == 0:
        return 1.0
    result = number
    i = 1

    while i * 2 <= power:
        result *= result
        i *= 2

    for _ in range(int(power) - i):
        result *= number

    return round(result, 11)


def power_degree_decomp(data: list) -> float:
    number = data[0]
    power = data[1]
    result = 1
    if power == 0:
        return 1.0
    while power > 1:
        if power % 2 == 1:
            result *= number
        number *= number
        power //= 2
    if power > 0:
        result *= number

    return round(result, 11)
