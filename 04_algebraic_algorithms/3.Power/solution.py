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
        answer = float(
            open(f'{TEST_PATH}\\{test_out[one_case]}', "r").read().strip())
        with open(f'{TEST_PATH}\\{test_in[one_case]}', "r") as test_file:
            data = [float(line.rstrip('\n')) for line in test_file]

        start_time = dt.datetime.now()

        # here the main function
        result = power_iteraction(data)

        func_time = (dt.datetime.now() - start_time).total_seconds() * 1000
        output_text = f'{test_in[one_case][:-3]} run with {func_time} ms, ' \
                      f'finished with {result == answer} result'
        if result == answer:
            print(colored(output_text, 'green'))

        else:
            print(f'data {data}')
            print(f'my result {result}')
            print(f'answer {answer}')
            print(colored(output_text, 'red'))
        print('----------------------------------------------------')


def power(data: list) -> float:
    number = data[0]
    power = data[1]
    if power == 0:
        return 1.0
    return round(number ** power, 11)


def power_iteraction(data: list) -> float:
    number = data[0]
    power = data[1]
    if power == 0:
        return 1.0

    result = number
    for _ in range(1, int(power)):
        result = result * number
    return round(result, 11)

def power(data: list) -> float:
    number = data[0]
    power = data[1]
    if power == 0:
        return 1.0
    return round(number ** power, 11)

def main():
    test_in, test_out = find_test_cases()
    make_tests(test_in, test_out)


if __name__ == '__main__':
    main()
