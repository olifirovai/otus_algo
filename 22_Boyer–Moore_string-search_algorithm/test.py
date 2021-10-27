import datetime as dt
import json
import os

from natsort import os_sorted
from termcolor import colored

from solution import StringSearch

TEST_PATH = f'{os.getcwd()}\\tests'
FUNC_DICT = {'find_full_scan': 'Searching with full scan',
             'find_jumper': 'Searching with Jump',
             'boyer_moore_match': 'Boyer-Moore algorithm', }

TEST_TIMES = ['10', '100', '1000', '10000']
TEST_AMOUNT = 8


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
    if 'result_dict.txt' not in os.listdir(os.getcwd()):
        create_dict_txt(test_in, FUNC_DICT)

    for func in FUNC_DICT.keys():
        start_text = f'Tests with function {func}'
        print(colored(start_text, 'magenta', attrs=['bold']))
        print('----------------------------------------------------')

        for one_case in range(len(test_in)):
            with open(f'{TEST_PATH}\\{test_in[one_case]}', "r") as test_file:
                value_list = test_file.readlines()
                text_value = value_list[0][:-1]
                pattern_value = value_list[1]
            with open(f'{TEST_PATH}\\{test_out[one_case]}', "r") as test_file:
                answer = int(test_file.read())

            start_time = dt.datetime.now()

            # here the main functions
            for once in TEST_TIMES:
                for _ in range(int(once)):
                    search_node = StringSearch(text_value, pattern_value)
                    result = eval(f'search_node.{func}()')
                func_time = (
                                    dt.datetime.now() - start_time).total_seconds() * 1000

                load_data_txt(one_case, FUNC_DICT, func, func_time, once)

                output_text = f'{test_in[one_case][:-3]} run with {func_time} ms, ' \
                              f'finished with {result == answer} result'
                if result == answer:
                    print(colored(output_text, 'green'))

                else:
                    print(f'my result {result}')
                    print(f'answer    {answer}')
                    print(colored(output_text, 'red'))
            print('----------------------------------------------------')
    print_table_readme('result_dict.txt')


def create_dict_txt(test_in, func_dict):
    with open('result_dict.txt', 'w') as s:
        result_dict = {}
        for func in func_dict.values():
            result_dict[func] = {}
            for amount in TEST_TIMES:
                result_dict[func][amount] = {}
                for test in range(len(test_in) // len(TEST_TIMES)):
                    result_dict[func][amount][str(test)] = 'Too much'
        s.write(json.dumps(result_dict))


def load_data_txt(one_case, func_dict, func, func_time, test_amount):
    with open('result_dict.txt', 'r') as f:
        data = f.read()
        result_dict = json.loads(data)

    with open('result_dict.txt', 'w') as s:
        test_num = f'{one_case}'
        func_disc = func_dict[func]
        result_dict[func_disc][test_amount][test_num] = func_time
        s.write(json.dumps(result_dict))


def print_table_readme(file):
    with open(file, 'r') as f:
        data = f.read()
        result_dict = json.loads(data)

    list_sort = list(result_dict.keys())
    header = '|Times|Test №|'
    header_line = '|---|---|'
    for one_sort in list_sort:
        header += f'{one_sort}|'
        header_line += '---|'
    print(header)
    print(header_line)
    for test in range(TEST_AMOUNT):
        for once in TEST_TIMES:
            line = f'|{once}|{test}'
            for sort in list_sort:
                time = result_dict[sort][once][str(test)]
                line += f'|{round(time, 2)} ms'
            print(f'{line}|')


def main():
    test_in, test_out = find_test_cases()
    make_tests(test_in, test_out)


if __name__ == '__main__':
    main()
