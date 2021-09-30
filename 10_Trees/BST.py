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
            return self.value
        elif self.value > search_value:
            if self.left is None:
                return f'{search_value} is not in a Tree'
            return self.left.search(search_value)
        else:
            if self.right is None:
                return f'{search_value} is not in a Tree'
            return self.right.search(search_value)

    def remove(self, root, remove_value):
        if self.value == remove_value:
            if not self.left:
                temp = self.right
                root = Node(self.right.value, self.right.left,
                            self.right.right)
                self.value = root.value
                root.right = None
                return
            elif not self.right:
                pass

            root = Node(self.value, self.left, self.right)
            # the biggest in the left subtree
            last_right_in_left = root.left

            while last_right_in_left.right:
                last_right_in_left = last_right_in_left.right
            return root.remove(last_right_in_left, remove_value)


        elif self.value > remove_value:
            if self.left is None:
                return f'{remove_value} is not in a Tree'
            return self.left.remove(root, remove_value)
        else:
            if self.right is None:
                return f'{remove_value} is not in a Tree'
            return self.right.remove(root, remove_value)

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
    root = Node(50)
    # number_list = list(set(round(random.random() * 100) for _ in range(20)))
    number_list = [3, 37, 38, 71, 8, 9, 10, 73, 45, 49, 82, 51, 23, 25, 91, 30,
                   63]
    for number in number_list:
        root.insert(number)
    # print(check_if_bst(root))
    print(root.search(8))
    print(root.search(16))
    print(root.remove(root, 8))
    print(root.remove(root, 16))

    # root.print_tree()
