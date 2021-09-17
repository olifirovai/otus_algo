import datetime as dt
import os

from termcolor import colored
from solution import (euclid_subtracting, steinitz_algorithm, euclid_division)  # noqa

TEST_PATH = f'{os.getcwd()}\\tests'

FUNC_DICT = {'euclid_subtracting': 'Euclid\'s Algorithm of Subtraction',
             'euclid_division': 'Euclid\'s Division Algorithm',
             'steinitz_algorithm': 'Steinitz-based algorithm'}


# find all files with in and out data
def find_test_cases():
    test_in = []
    test_out = []

    for dirpath, dirnames, filenames in os.walk(TEST_PATH):
        for filename in filenames:
            if filename.endswith('in'):
                test_in.append(filename)
            elif filename.endswith('out'):
                test_out.append(filename)

    return test_in, test_out


def make_tests(test_in: list, test_out: list) -> None:
    for func in FUNC_DICT.keys():
        print(colored(f'Tests with function {func}', 'magenta', attrs=['bold']))

        for one_case in range(6):
            with open(f'{TEST_PATH}\\{test_in[one_case]}', "r") as test_file:
                data = [int(line.rstrip('\n')) for line in test_file]
            answer = int(
                open(f'{TEST_PATH}\\{test_out[one_case]}', "r").read().strip())

            start_time = dt.datetime.now()

            # here the main function
            result = eval(f'{func}({data})')

            func_time = (dt.datetime.now() - start_time).total_seconds() * 1000
            output_text = f'{test_in[one_case][:-3]} run with {func_time} ms, ' \
                          f'finished with {result == answer} result'
            if result == answer:
                print(colored(output_text, 'green'))

            else:
                print(colored(output_text, 'red'))
            print('----------------------------------------------------')


def main():
    test_in, test_out = find_test_cases()
    make_tests(test_in, test_out)


if __name__ == '__main__':
    main()
