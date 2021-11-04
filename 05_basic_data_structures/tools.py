import json
import ast

CLASS_DICT = {'SingleArray': 'Single Array', 'VectorArray': 'Vector Array',
              'FactorArray': 'Factor Array', 'MatrixArray': 'Matrix Array'}

LENGTH_ARRAY = [10, 100, 1000, 10000]

FUNCTIONS = {'put': 'Put at the end', 'put_at': 'Put at the middle index',
             'put_at_0': 'Put at the 0 index',
             'delete': 'Delete end index',
             'delete_at': 'Delete middle index',
             'delete_at_0': 'Delete 0 index'}

with open('test_arrays.txt', 'r') as f:
    data = f.read()
    TEST_ARRAYS = ast.literal_eval(data)


def create_dict_txt():
    with open('result_dict.txt', 'w') as s:
        result_dict = {}
        for type_class in CLASS_DICT.values():
            result_dict[type_class] = {}
            for func in FUNCTIONS.values():
                result_dict[type_class][func] = {}
                for count in LENGTH_ARRAY:
                    result_dict[type_class][func][count] = "0 ms"
        s.write(json.dumps(result_dict))


def print_table_readme():
    with open('result_dict.txt', 'r') as f:
        data = f.read()
        result_dict = json.loads(data)

    header = '|Class|Count|Function|Time ms|'
    header_line = '|---|---|---|---|'
    print(header)
    print(header_line)

    for count in LENGTH_ARRAY:

        for func in FUNCTIONS.values():
            for class_name in CLASS_DICT.values():
                time_func = result_dict[class_name][func][str(count)]
                line = f'|{class_name}|{count}|{func}|{time_func}|'
                print(line)
            line = f'|------------|-------------|------------|-------------|'
            print(line)
