import datetime as dt
import json
import os

from natsort import os_sorted
from termcolor import colored

from solution import (bubble_sort, selection_sort, heap_sort, heapify,  # noqa
                      insertion_sort, shell_sort)  # noqa

LENGTH_LIST = {'0': 1, '1': 10, '2': 100, '3': 1000, '4': 10000, '5': 100000, '6': 1000000, '7': 10000000}
TEST_PATH = f'{os.getcwd()}\\tests'
FUNC_DICT = {'bubble_sort': 'Bubble sort',
             'selection_sort': 'Selection sort',
             'insertion_sort': 'Insertion sort',
             'shell_sort': 'Shell sort', 'heap_sort': 'Heap sort'}
TYPE_TEST = ['random', 'digits', 'sorted', 'revers']


# find all files with in and out data
def find_test_cases():
    test_in = []
    test_out = []

    folder_names = os_sorted(os.listdir(TEST_PATH))
    for folder in folder_names:
        filenames = os_sorted(os.listdir(f'{TEST_PATH}\\{folder}'))
        for filename in filenames:
            if filename.endswith('in'):
                test_in.append(f'{folder}\\{filename}')
            elif filename.endswith('out'):
                test_out.append(f'{folder}\\{filename}')
    return test_in, test_out


def make_tests(test_in: list, test_out: list) -> None:
    if 'result_dict.txt' not in os.listdir(os.getcwd()):
        create_dict_txt(test_in, FUNC_DICT)

    for func in FUNC_DICT.keys():
        if func != 'bubble_sort':
            continue
        print(
            colored(f'Tests with function {func}', 'magenta', attrs=['bold']))
        print('----------------------------------------------------')

        for one_case in range(len(test_in)):
            with open(f'{TEST_PATH}\\{test_in[one_case]}', "r") as test_file:
                count = 0
                for line in test_file:
                    if count == 0:
                        n = int(line)
                        count += 1
                    else:
                        array = [int(x) for x in line.split()]
            with open(f'{TEST_PATH}\\{test_out[one_case]}', "r") as test_file:
                for line in test_file:
                    answer = [int(x) for x in line.split()]
            if n > 100000:
                continue
            start_time = dt.datetime.now()

            # here the main functions

            result = eval(f'{func}({n}, {array})')
            func_time = (dt.datetime.now() - start_time).total_seconds() * 1000

            load_data_txt(test_in, one_case, FUNC_DICT, func, func_time)

            output_text = f'{test_in[one_case][:-3]} run with {func_time} ms, ' \
                          f'finished with {result == answer} result'
            if result == answer:
                print(colored(output_text, 'green'))

            else:
                print(colored(output_text, 'red'))
            print('----------------------------------------------------')
    print_table_readme('result_dict.txt')


def load_data_txt(test_in, one_case, func_dict, func, func_time):
    with open('result_dict.txt', 'r') as f:
        data = f.read()
        result_dict = json.loads(data)

    with open('result_dict.txt', 'w') as s:
        type_test = f'{test_in[one_case][2:8]}'
        test_num = f'{test_in[one_case][14]}'
        result_dict[func_dict[func]][type_test][test_num] = func_time
        s.write(json.dumps(result_dict))


def create_dict_txt(test_in, func_dict):
    with open('result_dict.txt', 'w') as s:
        result_dict = {}
        for func in func_dict.values():
            result_dict[func] = {}
            for one_type in TYPE_TEST:
                result_dict[func][one_type] = {}
                for test in range(len(test_in) // len(TYPE_TEST)):
                    result_dict[func][one_type][str(test)] = 'Too much'
        s.write(json.dumps(result_dict))


def print_table_readme(file):
    with open(file, 'r') as f:
        data = f.read()
        result_dict = json.loads(data)
    header = '|Test Type|Length Array|Test №|Bubble sort|Insertion sort' \
             '|Selection sort|Shell sort|Heap sort|'
    header_line = '|---|---|---|---|---|---|---|---|'
    print(header)
    print(header_line)

    for one_type in TYPE_TEST:
        for test in range(len(list(LENGTH_LIST.keys()))):
            line = f'|{one_type}|{LENGTH_LIST[str(test)]}|{test}'
            for func in FUNC_DICT.values():
                time = result_dict[func][one_type][str(test)]
                line += f'|{time} ms'
            print(f'{line}|')


def main():
    test_in, test_out = find_test_cases()
    make_tests(test_in, test_out)


if __name__ == '__main__':
    main()
