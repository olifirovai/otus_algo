import datetime as dt
import os
import importlib
from natsort import os_sorted
from termcolor import colored
from solution import (fib_recursive, golden_ratio, fib_iteration, # noqa
                      fib_matrix)  # noqa

tools = importlib.import_module('04_algebraic_algorithms.tools')

TEST_PATH = f'{os.getcwd()}\\tests'

FUNC_DICT = {'fib_recursive': 'Recursion',
             'golden_ratio': 'Golden ratio',
             'fib_iteration': 'Iteration',
             'fib_matrix': 'Matrix exponentiation'}


# find all files with in and out data
def find_test_cases():
    test_in = []
    test_out = []
    filenames = os_sorted(os.listdir(f'{TEST_PATH}'))
    for filename in filenames:
        if filename.endswith('in'):
            test_in.append(filename)
        elif filename.endswith('out'):
            test_out.append(filename)
    return test_in, test_out


def make_tests(test_in: list, test_out: list) -> None:
    if 'result_dict.txt' not in os.listdir(os.getcwd()):
        tools.create_dict_txt(test_in, FUNC_DICT)

    for func in FUNC_DICT.keys():
        print(
            colored(f'Tests with function {func}', 'magenta', attrs=['bold']))

        for one_case in range(7):
            data = int(open(f'{TEST_PATH}\\{test_in[one_case]}', "r").read())
            answer = int(
                open(f'{TEST_PATH}\\{test_out[one_case]}', "r").read().strip())

            start_time = dt.datetime.now()

            # here the main function
            result = eval(f'{func}({data})')

            func_time = (dt.datetime.now() - start_time).total_seconds() * 1000
            tools.load_data_txt(one_case, FUNC_DICT, func, func_time)
            output_text = f'{test_in[one_case][:-3]} run with {func_time} ms, ' \
                          f'finished with {result == answer} result'
            if result == answer:
                print(colored(output_text, 'green'))

            else:
                print(f'data {data}')
                print(f'my result {str(result)[:60]}')
                print(f'answer {str(answer)[:60]}')
                print(colored(output_text, 'red'))
            print('----------------------------------------------------')


def main():
    test_in, test_out = find_test_cases()
    make_tests(test_in, test_out)
    tools.print_table_readme('result_dict.txt', len(test_in))


if __name__ == '__main__':
    main()
