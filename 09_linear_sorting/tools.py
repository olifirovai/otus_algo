import json
import os
import struct

LENGTH_LIST = {'0': 10, '1': 1000, '2': 100000, '3': 1000000, '4': 10000000,
               '5': 100000000}

TEST_PATH = f'{os.getcwd()}\\tests'

FUNC_DICT = {'merge_sort': 'Merge sort',
             'mix_merge_quick_sort': 'Merge & Quick sort',
             'counting_sort': 'Counting sort', 'radix_sort': 'Radix sort',
             'bucket_sort': 'Bucket sort'}


def create_dict_txt(test_in, func_dict):
    with open('result_dict.txt', 'w') as s:
        result_dict = {}
        for func in func_dict.values():
            result_dict[func] = {}
            for test in range(len(test_in)):
                test_num = f'{test}'
                result_dict[func][test_num] = 'Too much'
        s.write(json.dumps(result_dict))


def load_data_txt(one_case, func_dict, func, func_time):
    with open('result_dict.txt', 'r') as f:
        data = f.read()
        result_dict = json.loads(data)

    with open('result_dict.txt', 'w') as s:
        test_num = f'{one_case}'
        func_disc = func_dict[func]
        result_dict[func_disc][test_num] = func_time
        s.write(json.dumps(result_dict))


def print_table_readme(file):
    with open(file, 'r') as f:
        data = f.read()
        result_dict = json.loads(data)

    list_sort = list(result_dict.keys())
    header = '|Test №|Length Array|'
    header_line = '|---|---|'
    for one_sort in list_sort:
        header += f'{one_sort}|'
        header_line += '---|'
    print(header)
    print(header_line)

    for test in range(len((list(LENGTH_LIST.keys())))):
        line = f'|{test}|{LENGTH_LIST[str(test)]}'
        for sort in list_sort:
            time = result_dict[sort][str(test)]
            line += f'|{time} ms'
        print(f'{line}|')


def unpack_bin_file(data: bytes, length: int) -> list:
    number_list = list(struct.unpack(f'@{length}h', data))

    # make integers between 0 and 65536
    for i in range(len(number_list)):
        number_list[i] += 2 ** 15

    return number_list


def pack_bin_file(sorted_list, length: int):
    test_number = list(LENGTH_LIST.values()).index(length)
    new_bin_file = open(f'{TEST_PATH}\\test.{test_number}.out', 'wb')

    # make integers between -32768 and 32768
    for i in range(length):
        sorted_list[i] -= 2 ** 15

    bin_list = struct.pack(f'@{length}h', *sorted_list)
    new_bin_file.write(bin_list)
