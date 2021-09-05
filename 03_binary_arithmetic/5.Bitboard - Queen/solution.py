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
        result = list(queen_turn(data))

        func_time = (dt.datetime.now() - start_time).total_seconds() * 1000
        output_text = f'{test_in[one_case][:-3]} run with {func_time} ms, ' \
                      f'finished with {result == answer} result'
        if result == answer:
            print(colored(output_text, 'green'))

        else:
            print(colored(output_text, 'red'))
        print('----------------------------------------------------')


def queen_turn(position: int) -> Tuple[int, int]:
    queen = 1 << position
    no_a = 0xfefefefefefefefe
    no_h = 0x7f7f7f7f7f7f7f7f
    whole_board = 0xffffffffffffffff

    # vertical & horizontal move
    left_move = (queen >> 1) & no_h
    right_move = (queen << 1) & no_a
    up_move = queen << 8
    down_move = queen >> 8

    # diagonal move
    up_left_move = (queen << 7) & no_h
    up_right_move = (queen << 9) & no_a
    down_left_move = (queen >> 9) & no_h
    down_right_move = (queen >> 7) & no_a

    for _ in range(7):
        left_move = (left_move | left_move >> 1) & no_h
        right_move = (right_move | right_move << 1) & no_a
        up_move = up_move | up_move << 8
        down_move = down_move | down_move >> 8
        up_left_move = (up_left_move | up_left_move << 7) & no_h
        up_right_move = (up_right_move | up_right_move << 9) & no_a
        down_left_move = (down_left_move | down_left_move >> 9) & no_h
        down_right_move = (down_right_move | down_right_move >> 7) & no_a

    ver_hor_move = (down_move | up_move | left_move | right_move)
    diagonal_move = (
            up_left_move | up_right_move | down_left_move | down_right_move)
    moves = (ver_hor_move | diagonal_move) & whole_board

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
