import datetime as dt

from natsort import os_sorted
from termcolor import colored

from solution import *  # noqa
from tools import *

AMOUNT_TESTS = 3


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
        create_dict_txt(test_in, FUNC_DICT)

    for func in FUNC_DICT.keys():
        # if func != 'radix_sort':
        #     continue
        print(
            colored(f'Tests with function {func}', 'magenta', attrs=['bold']))
        print('----------------------------------------------------')

        for one_case in range(AMOUNT_TESTS):
            length = LENGTH_LIST[f'{one_case}']
            # if length != 100000000:
            #     continue
            data = open(f'{TEST_PATH}\\{test_in[one_case]}', "rb").read()
            data = unpack_bin_file(data, length)
            answer = open(f'{TEST_PATH}\\{test_out[one_case]}', "rb").read()
            answer = unpack_bin_file(answer, length)
            start_time = dt.datetime.now()

            # here the main function
            result = eval(f'{func}({data})')

            func_time = (dt.datetime.now() - start_time).total_seconds() * 1000
            load_data_txt(one_case, FUNC_DICT, func, func_time)
            output_text = f'{test_in[one_case][:-3]} run with {func_time} ms, ' \
                          f'finished with {result == answer} result'
            if result == answer:
                print(colored(output_text, 'green'))

            else:
                # print(f'data {data}')
                # print(f'my result {result}')
                # print(f'answer {answer}')
                print(colored(output_text, 'red'))
            print('----------------------------------------------------')


def main():
    # test_in, test_out = find_test_cases()
    # make_tests(test_in, test_out)
    print_table_readme('result_dict.txt', )


if __name__ == '__main__':
    main()
