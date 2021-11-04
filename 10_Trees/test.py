from BTS import Node as BTSTree  # noqa

from AVL import Node as AVLTree  # noqa

LENGTH_LIST = {'0': 10, '1': 1000, '2': 100000, '3': 1000000, '4': 10000000,
               '5': 100000000}

# TODO дз Двоичные деревья поиска АВЛ

# Создать два дерева(максимальный размер дерева выберите такой, чтобы программа
# работала не дольше 1 минуты)
def make_tree():
    pass


# Добавить N чисел в случайном порядке.
def add_numbers_random(size):
    pass


# Добавить N чисел в возрастающем порядке.
def add_numbers_increasing(size):

    for i in range(size+1):
        tree = BTSTree()
    pass


# Искать N / 10 случайных чисел в каждом дереве.
def search_every_ten(tree):
    pass


# Удалить N / 10 случайных элементов в каждом дереве.
def delete_every_ten(tree):
    pass


def main():
    tree = make_tree()
    search_every_ten(tree)
    delete_every_ten(tree)


if __name__ == '__main__':
    main()
