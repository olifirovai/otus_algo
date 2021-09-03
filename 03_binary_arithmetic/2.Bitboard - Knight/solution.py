import datetime as dt
import os
from typing import Tuple

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
        with open(f'{TEST_PATH}\\{test_out[one_case]}', "r") as test_file:
            answer = [int(line.rstrip('\n')) for line in test_file]
        data = int(
            open(f'{TEST_PATH}\\{test_in[one_case]}', "r").read().strip())

        start_time = dt.datetime.now()

        # here the main function
        result = list(knight_turn(data))

        func_time = (dt.datetime.now() - start_time).total_seconds() * 1000
        output_text = f'{test_in[one_case][:-3]} run with {func_time} ms, ' \
                      f'finished with {result == answer} result'
        if result == answer:
            print(colored(output_text, 'green'))

        else:
            print(f'data = {data}')
            print(f'answer = {answer}')
            print(f'my result = {result}')
            print(colored(output_text, 'red'))
        print('----------------------------------------------------')


def knight_turn(position: int) -> Tuple[int, int]:
    knight = 1 << position
    no_a_b = 0xfcfcfcfcfcfcfcfc
    no_b = 0xfdfdfdfdfdfdfdfd
    no_h = 0x7f7f7f7f7f7f7f7f
    no_g = 0xbfbfbfbfbfbfbfbf

    knight_a = knight & no_g & no_h
    knight_b = knight & no_h
    knight_g = knight & no_a
    knight_h = knight & no_a & no_b

    moves = ((knight_b << 17) | (knight_g << 15) |
(knight_a << 10) |                              (knight_h << 6) |
(knight_a >> 10) |                              (knight_h >> 6) |
             (knight_b >> 17) | (knight_g >> 15))

    return count_bits(moves), moves


def count_bits(moves):
    count = 0
    while moves > 0:
        count += 1
        moves &= moves - 1
    return count


def main():
    test_in, test_out = find_test_cases()
    make_tests(test_in, test_out)


if __name__ == '__main__':
    main()
