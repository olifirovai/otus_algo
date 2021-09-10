import datetime as dt
import os

from natsort import os_sorted
from termcolor import colored

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

        start_time = dt.datetime.now()

        # here the main function
        result = insertion_sort(n, array)

        func_time = (dt.datetime.now() - start_time).total_seconds() * 1000
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


def bubble_sort(n: int, array: list) -> list:
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]

    return array


def selection_sort(n: int, array: list) -> list:
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if array[min_index] > array[j]:
                min_index = j
        array[i], array[min_index] = array[min_index], array[i]
    return array


def insertion_sort(n: int, array: list) -> list:
    for i in range(1, n):
        j = i - 1

        while j >= 0 and array[i] < array[j]:
            array[i], array[j] = array[j], array[i]
            j -= 1
            i -= 1

    return array


def main():
    test_in, test_out = find_test_cases()
    make_tests(test_in, test_out)


if __name__ == '__main__':
    main()
