import datetime as dt
import os
import importlib
from natsort import os_sorted
from termcolor import colored
from solution import (simple_power, power_iteration, power_two, power_degree_decomp)  # noqa

tools = importlib.import_module('04_algebraic_algorithms.tools')

TEST_PATH = f'{os.getcwd()}\\tests'

FUNC_DICT = {'power_iteration': 'Iterations',
             'power_two': 'Power of two with a multiplies',
             'power_degree_decomp': 'Binary decomposition of the power value'}


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
        print(colored(f'Tests with function {func}', 'magenta', attrs=['bold']))

        for one_case in range(9):
            with open(f'{TEST_PATH}\\{test_in[one_case]}', "r") as test_file:
                data = [float(line.rstrip('\n')) for line in test_file]
            answer = float(
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
                print(f'my result {result}')
                print(f'answer {answer}')
                print(colored(output_text, 'red'))
            print('----------------------------------------------------')


def main():
    test_in, test_out = find_test_cases()
    make_tests(test_in, test_out)
    tools.print_table_readme('result_dict.txt', )

if __name__ == '__main__':
    main()
