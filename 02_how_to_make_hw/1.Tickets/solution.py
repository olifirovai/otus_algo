import datetime as dt
import os

from termcolor import colored

TEST_PATH = f'{os.getcwd()}\\tests'


# find all files with in and out data
def find_test_cases():
    test_in = []
    test_out = []

    for dirpath, dirnames, filenames in os.walk(TEST_PATH):
        for filename in filenames:
            if filename.endswith('in'):
                test_in.append(filename)
            elif filename.endswith('out'):
                test_out.append(filename)

    return test_in, test_out


def make_tests(test_in: list, test_out: list) -> None:
    for one_case in range(len(test_in)):
        answer = int(open(f'{TEST_PATH}\\{test_out[one_case]}', 'r').read())
        data = int(
            open(f'{TEST_PATH}\\{test_in[one_case]}', 'r').read().strip())

        start_time = dt.datetime.now()

        # here the main function
        result = sum([x ** 2 for x in lucky_tickets(data)])

        func_time = (dt.datetime.now() - start_time).total_seconds() * 1000
        output_text = f'{test_in[one_case][:-3]} run with {func_time} ms, ' \
                      f'finished with {result == answer} result'
        if result == answer:
            print(colored(output_text, 'green'))

        else:
            print(colored(output_text, 'red'))
        print('----------------------------------------------------')


def lucky_tickets(n: int, line=[1]):
    new_line = []
    if n > 1:
        line = lucky_tickets(n - 1, line)

    for i in range(9 * n + 1):
        new = 0
        for j in range(max(0, len(line) - 1 - i),
                       min(len(line), 9 * n + 1 - i)):
            new += line[j]
        new_line.append(new)

    # return the last list which is consisted of sums for the half of the
    # whole ticket
    # ex. for n = 2: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    return new_line


def main():
    test_in, test_out = find_test_cases()
    make_tests(test_in, test_out)


if __name__ == '__main__':
    main()
