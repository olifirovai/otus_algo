import datetime as dt
import json
import os

from natsort import os_sorted
from termcolor import colored

from solution import (bubble_sort, selection_sort, heap_sort, heapify,  # noqa
                      insertion_sort, shell_sort)  # noqa

TEST_PATH = f'{os.getcwd()}\\tests'


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
        if n != 100000:
            continue
        start_time = dt.datetime.now()

        # here the main functions
        func_dict = {'bubble_sort': 'Bubble sort',
                     'selection_sort': 'Selection sort',
                     'insertion_sort': 'Insertion sort',
                     'shell_sort': 'Shell sort', 'heap_sort': 'Heap sort'}

        for func in func_dict.keys():
            if func != 'heap_sort':
                continue
            result = eval(f'{func}({n}, {array})')

            func_time = (dt.datetime.now() - start_time).total_seconds() * 1000

            load_data_txt(test_in, one_case, func_dict, func, func_time)

            output_text = f'{test_in[one_case][:-3]} run with {func_time} ms, ' \
                          f'finished with {result == answer} result'
            if result == answer:
                print(colored(output_text, 'green'))

            else:
                # print(f'data {array}')
                # print(f'my result {result}')
                # print(f'answer {answer}')
                print(colored(output_text, 'red'))
            print('----------------------------------------------------')


def load_data_txt(test_in, one_case, func_dict, func, func_time):
    with open('result_dict.txt', 'r') as f:
        data = f.read()
        result_dict = json.loads(data)

    with open('result_dict.txt', 'w') as s:
        type_test = f'{test_in[one_case][2:8]}'
        test_num = f'{test_in[one_case][14]}'
        result_dict['Type sort'][func_dict[func]][type_test][
            test_num] = func_time
        s.write(json.dumps(result_dict))


def print_table_readme(file):
    with open(file, 'r') as f:
        data = f.read()
        result_dict = json.loads(data)
    header = '|Test Type|Test №|Bubble sort|Insertion sort' \
             '|Selection sort|Shell sort|Heap sort|'
    header_line = '|---|---|---|---|---|---|---|'
    print(header)
    print(header_line)
    list_sort = ['Bubble sort', 'Insertion sort', 'Selection sort',
                 'Shell sort', 'Heap sort']
    type_test = ['random', 'digits', 'sorted', 'revers']

    for one_type in type_test:
        for test in range(8):
            line = f'|{one_type}|{test}'
            for sort in list_sort:
                time = result_dict['Type sort'][sort][one_type][str(test)]
                line += f'|{time} ms'
            print(f'{line}|')


def main():
    file = 'result_dict.txt'
    print_table_readme(file)

    # test_in, test_out = find_test_cases()
    # make_tests(test_in, test_out)


if __name__ == '__main__':
    main()
