class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.right = right
        self.left = left

    def __str__(self):
        return self.value

    def insert(self, insert_value):
        if self.value > insert_value:
            if self.left is None:
                self.left = Node(insert_value)
            else:
                self.left.insert(insert_value)
        else:
            if self.right is None:
                self.right = Node(insert_value)
            else:
                self.right.insert(insert_value)

    def search(self, search_value):
        if self.value == search_value:
            return self
        elif self.value > search_value:
            if self.left is None:
                return f'{search_value} is not in a Tree'
            return self.left.search(search_value)
        else:
            if self.right is None:
                return f'{search_value} is not in a Tree'
            return self.right.search(search_value)

    def remove(self, remove_value):
        if self is None:
            return self
        if remove_value == self.value:
            if not self.left and not self.right:
                self = None
                return self

            if not self.left:
                temp = self.right
                self.right = None
                return temp

            elif not self.right:
                temp = self.left
                self.left = None
                return temp

            # the biggest in the left subtree
            last_right_in_left = self.left.find_max_in_left()
            self.value = last_right_in_left.value
            last_right_in_left.remove(self.value)


        elif remove_value < self.value:
            if self.left is None:
                print( f'{remove_value} is not in a Tree')
            else:
                self.left = self.left.remove(remove_value)
        else:
            if self.right is None:
                print( f'{remove_value} is not in a Tree')
            else:
                self.right = self.right.remove(remove_value)

        return self

    def find_max_in_left(self):
        current = self
        while self.right:
            current = self.right
        return current

    def print_tree(self):
        if self.left:
            self.left.print_tree()
        print(self.value)
        if self.right:
            self.right.print_tree()


def check_if_bst(root):
    if root is None:
        return True

    if root.left is not None and root.left.value >= root.value:
        return False

    if root.right is not None and root.right.value <= root.value:
        return False

    return check_if_bst(root.left) and check_if_bst(root.right)


if __name__ == "__main__":
    root = Node(59)
    # number_list = list(set(round(random.random() * 100) for _ in range(20)))
    number_list = [45, 75, 40, 51, 71, 77, 35, 42, 47, 53, 41, 43, 46, 49, 52,
                   55]
    for number in number_list:
        root.insert(number)
    print(check_if_bst(root))
    # print(root.search(8))
    print(root.search(16))
    root.remove(55)
    root.remove(51)
    # print(root.remove(root, 16))
    root.remove(10)
    print()
    root.print_tree()
