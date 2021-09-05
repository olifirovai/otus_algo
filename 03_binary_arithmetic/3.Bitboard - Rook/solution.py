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
        result = list(rook_turn(data))

        func_time = (dt.datetime.now() - start_time).total_seconds() * 1000
        output_text = f'{test_in[one_case][:-3]} run with {func_time} ms, ' \
                      f'finished with {result == answer} result'
        if result == answer:
            print(colored(output_text, 'green'))

        else:
            print(colored(output_text, 'red'))
        print('----------------------------------------------------')


def rook_turn(position: int) -> Tuple[int, int]:
    rook = 1 << position
    no_a = 0xfefefefefefefefe
    no_h = 0x7f7f7f7f7f7f7f7f
    whole_board = 0xffffffffffffffff

    left_move = (rook >> 1) & no_h
    right_move = (rook << 1) & no_a
    up_move = rook << 8
    down_move = rook >> 8

    for _ in range(7):
        left_move = (left_move | left_move >> 1) & no_h
        right_move = (right_move | right_move << 1) & no_a
        up_move = up_move | up_move << 8
        down_move = down_move | down_move >> 8

    moves = (down_move | up_move | left_move | right_move) & whole_board

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
