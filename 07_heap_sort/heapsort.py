import datetime as dt
import os

from natsort import os_sorted
from termcolor import colored

TEST_PATH = f'{os.getcwd()}\\tests'


def heapSort(n, array):
    for i in range(n // 2 - 1, -1, -1):
        heapify(n, i, array)

    for i in range(n - 1, 0, -1):
        array[i], array[0] = array[0], array[i]  # swap
        heapify(i, 0, array)
    return array


def heapify(n: int, root: int, array: list):
    left_child = 2 * root + 1
    right_child = 2 * root + 2
    x = root
    if left_child < n and array[left_child] > array[x]:
        x = left_child
    if right_child < n and array[right_child] > array[x]:
        x = right_child
    if x != root:
        array[root], array[x] = array[x], array[root]
        heapify(n, x, array)


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
        result = heapSort(n, array)

        func_time = (dt.datetime.now() - start_time).total_seconds() * 1000
        output_text = f'{test_in[one_case][:-3]} run with {func_time} ms, ' \
                      f'finished with {result == answer} result'
        if result == answer:
            print(colored(output_text, 'green'))

        else:
            print(colored(output_text, 'red'))
        print('----------------------------------------------------')


def main():
    test_in, test_out = find_test_cases()
    make_tests(test_in, test_out)


if __name__ == '__main__':
    main()
