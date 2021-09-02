import datetime as dt
import os

from termcolor import colored


# find all files with in and out data
def find_test_cases():
    test_in = []
    test_out = []

    for dirpath, dirnames, filenames in os.walk(os.getcwd()):
        for filename in filenames:
            if filename.endswith('in'):
                test_in.append(filename)
            elif filename.endswith('out'):
                test_out.append(filename)

    return test_in, test_out


def make_tests(test_in: list, test_out: list) -> None:
    for one_case in range(len(test_in)):
        answer = int(open(test_out[one_case], "r").read())
        data = int(open(test_in[one_case], "r").read().strip())

        start_time = dt.datetime.now()

        # here the main function
        result = queen_turn(data)

        func_time = (dt.datetime.now() - start_time).total_seconds() * 1000
        output_text = f'{test_in[one_case][:-3]} run with {func_time} ms, ' \
                      f'finished with {result == answer} result'
        if result == answer:
            print(colored(output_text, 'green'))

        else:
            print(colored(output_text, 'red'))
        print('----------------------------------------------------')


def queen_turn(n: int) -> int:
    pass


def main():
    test_in, test_out = find_test_cases()
    make_tests(test_in, test_out)


if __name__ == '__main__':
    main()
