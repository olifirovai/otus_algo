import json


def create_dict_txt(test_in, func_dict):
    with open('result_dict.txt', 'w') as s:
        result_dict = {}
        for func in func_dict.values():
            result_dict[func] = {}
            for test in range(len(test_in)):
                test_num = f'{test}'
                result_dict[func][test_num] = 'time'
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
    header = '|Test №|'
    header_line = '|---|'
    for one_sort in list_sort:
        header += f'{one_sort}|'
        header_line += '---|'
    print(header)
    print(header_line)

    for test in range(9):
        line = f'|{test}'
        for sort in list_sort:
            time = result_dict[sort][str(test)]
            line += f'|{time} ms'
        print(f'{line}|')
