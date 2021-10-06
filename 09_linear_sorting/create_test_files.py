import random

from test import (find_test_cases, )
from tools import *


def write_binary_file(length: int) -> list:
    number_list = list(int(random.random() * 2 ** 16) for _ in range(length))
    test_number = list(LENGTH_LIST.values()).index(length)
    new_bin_file = open(f'{TEST_PATH}\\test.{test_number}.in', 'wb')

    # make integers between -32768 and 32768
    for i in range(len(number_list)):
        number_list[i] -= 2 ** 15

    bin_list = struct.pack(f'@{length}h', *number_list)
    new_bin_file.write(bin_list)

    return number_list


def prepare_out_tests():
    test_in, _ = find_test_cases()
    for test in test_in:
        with open(f'{TEST_PATH}\\{test}', "rb") as test_file:
            data = test_file.read()
        length = LENGTH_LIST[test[5]]
        sorted_list = sorted(unpack_bin_file(data, length))
        pack_bin_file(sorted_list, length)


def check_all_tests():
    for test in range(6):
        with open(f'{TEST_PATH}\\test.{test}.in', "rb") as in_file:
            data_in = in_file.read()
            length = LENGTH_LIST[str(test)]
            unsorted_list = unpack_bin_file(data_in, length)
            print(f'test {test} unsorted_list {unsorted_list[:20]}')
            sorted_list = sorted(unsorted_list)
            print(f'test {test} in sorted_list {sorted_list[:20]}')

        with open(f'{TEST_PATH}\\test.{test}.out', "rb") as out_file:
            data_out = out_file.read()
            out_list = unpack_bin_file(data_out, length)
            print(f'test {test} out sorted_list {out_list[:20]}')
        print(sorted_list == out_list)


def main():
    for length in LENGTH_LIST.values():
        write_binary_file(length)
    prepare_out_tests()
    check_all_tests()


if __name__ == "__main__":
    main()

#
