from solution import (SingleArray, VectorArray, FactorArray,  # noqa
                      MatrixArray, )  # noqa
import datetime as dt
from termcolor import colored
from tools import *
import os


def array_put_test(length, class_name):
    print(colored(f'put', 'magenta', attrs=['bold']))
    array = eval(f'{class_name}()')
    start_time = dt.datetime.now()
    for number in TEST_ARRAYS[length]:
        array.put(number)

    func_time = (dt.datetime.now() - start_time).total_seconds() * 1000
    func_time = round(func_time, 3)
    print(colored('Done', 'blue'))

    return array, func_time


def array_put_at_test(length, class_name, middle=False):
    if middle:
        text = 'put at middle index'
    else:
        text = 'put at 0 index'
    print(colored(text, 'magenta', attrs=['bold']))

    array = eval(f'{class_name}()')
    for number in range(20):
        array.put(number)

    start_time = dt.datetime.now()

    for number in TEST_ARRAYS[length]:
        if middle:
            index = array.size() // 2
        else:
            index = 0
        array.put_at(number, index)

    func_time = (dt.datetime.now() - start_time).total_seconds() * 1000
    func_time = round(func_time, 3)
    print(colored('Done', 'blue'))

    return array, func_time


def array_delete_test(array):
    print(colored(f'delete', 'magenta', attrs=['bold']))
    start_time = dt.datetime.now()
    for _ in range(array.size()):
        array.delete()
    func_time = (dt.datetime.now() - start_time).total_seconds() * 1000
    func_time = round(func_time, 3)
    print(colored('Done', 'blue'))

    return func_time


def array_delete_at_test(array, middle=False):
    if middle:
        text = 'delete at middle index'
    else:
        text = 'delete at 0 index'
    print(colored(text, 'magenta', attrs=['bold']))

    start_time = dt.datetime.now()

    for _ in range(array.size()):
        if middle:
            index = array.size() // 2
        else:
            index = 0
        array.delete_at(index)

    func_time = (dt.datetime.now() - start_time).total_seconds() * 1000
    func_time = round(func_time, 3)
    print(colored('Done', 'blue'))

    return func_time


def main():
    if 'result_dict.txt' not in os.listdir(os.getcwd()):
        create_dict_txt()

    for length in LENGTH_ARRAY:

        print(
            colored(f'Array Length is {length}', 'yellow',
                    attrs=['bold', 'underline', 'dark']))

        for cl_name in CLASS_DICT.keys():
            print(colored(f'functions with {cl_name}', 'yellow',
                          attrs=['bold']))
            with open('result_dict.txt', 'r') as file:
                dict_data = file.read()
                result_dict = json.loads(dict_data)

            class_head = CLASS_DICT[cl_name]
            array, test_time = array_put_test(length, cl_name)
            result_dict[class_head][FUNCTIONS['put']][str(length)] = test_time

            test_time = array_delete_test(array)
            result_dict[class_head][FUNCTIONS['delete']][
                str(length)] = test_time

            array, test_time = array_put_at_test(length, cl_name)  # at 0 index

            result_dict[class_head][FUNCTIONS['put_at_0']][
                str(length)] = test_time

            test_time = array_delete_at_test(array)  # at 0 index

            result_dict[class_head][FUNCTIONS['delete_at_0']][
                str(length)] = test_time

            array, test_time = array_put_at_test(length, cl_name,
                                                 True)  # at middle index

            result_dict[class_head][FUNCTIONS['put_at']][
                str(length)] = test_time

            test_time = array_delete_at_test(array, True)  # at middle index

            result_dict[class_head][FUNCTIONS['delete_at']][
                str(length)] = test_time

            with open('result_dict.txt', 'w') as s:
                s.write(json.dumps(result_dict))

    print_table_readme()


if __name__ == '__main__':
    main()
