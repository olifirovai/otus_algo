import datetime as dt
import os
from decimal import Decimal, ROUND_FLOOR, InvalidOperation

from natsort import os_sorted
from termcolor import colored

TEST_PATH = f'{os.getcwd()}\\tests'


# find all files with in and out data
def find_test_cases():
    test_in = []
    test_out = []

    filenames = os_sorted(os.listdir(TEST_PATH))
    for filename in filenames:
        if filename.endswith('in'):
            test_in.append(filename)
        elif filename.endswith('out'):
            test_out.append(filename)
    return test_in, test_out


def make_tests(test_in: list, test_out: list) -> None:
    for one_case in range(len(test_in)):
        answer = int(
            open(f'{TEST_PATH}\\{test_out[one_case]}', "r").read().strip())
        data = int(
            open(f'{TEST_PATH}\\{test_in[one_case]}', "r").read().strip())

        start_time = dt.datetime.now()

        # here the main function
        result = golden_ratio(data)

        func_time = (dt.datetime.now() - start_time).total_seconds() * 1000
        output_text = f'{test_in[one_case][:-3]} run with {func_time} ms, ' \
                      f'finished with {result == answer} result'
        if result == answer:
            print(colored(output_text, 'green'))

        else:
            print(f'data {data}')
            print(f'my result {result}')
            print(f'answer {answer}')
            print(colored(output_text, 'red'))
        print('----------------------------------------------------')


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
    except InvalidOperation:
        pass

def main():
    test_in, test_out = find_test_cases()
    make_tests(test_in, test_out)


if __name__ == '__main__':
    main()
