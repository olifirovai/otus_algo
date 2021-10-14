from solution import (SingleArray, VectorArray, FactorArray,  # noqa
                      MatrixArray, )  # noqa
import importlib
import datetime as dt

tools = importlib.import_module('04_algebraic_algorithms.tools')

CLASS_DICT = {'SingleArray': 'Single Array', 'VectorArray': 'Vector Array',
              'FactorArray': 'Factor Array', 'MatrixArray': 'Matrix Array'}


def array_put_test():
    for class_name in CLASS_DICT.keys():
        if class_name != 'SingleArray':
            continue
        array = eval(f'{class_name}()')
        start_time = dt.datetime.now()
        for i in range(10001):
            array.put(i)
        func_time = (dt.datetime.now() - start_time).total_seconds() * 1000

        print(f'{func_time=}')


def array_put_at_test():
    for class_name in CLASS_DICT.keys():
        if class_name != 'SingleArray':
            continue
        array = eval(f'{class_name}()')
        for i in range(20):
            array.put(i)
        start_time = dt.datetime.now()
        for i in range(20):
            array.put_at(i, array.size() // 2)
            print(array.array)
        func_time = (dt.datetime.now() - start_time).total_seconds() * 1000

        print(f'{func_time=}')


def main():
    array_put_test()
    array_put_at_test()

if __name__ == '__main__':
    main()
