from solution import (SingleArray, VectorArray, FactorArray,  # noqa
                      MatrixArray, )  # noqa
import importlib
import datetime as dt

tools = importlib.import_module('04_algebraic_algorithms.tools')

CLASS_DICT = {'SingleArray': 'Single Array', 'VectorArray': 'Vector Array',
              'FactorArray': 'Factor Array', 'MatrixArray': 'Matrix Array'}


def array_put_test():
    for class_name in CLASS_DICT.keys():
        array = eval(f'{class_name}()')
        start_time = dt.datetime.now()
        for i in range(10001):
            array.put(i)
        func_time = (dt.datetime.now() - start_time).total_seconds() * 1000

        print(f'{func_time=}')


def main():
    array_put_test()


if __name__ == '__main__':
    main()
