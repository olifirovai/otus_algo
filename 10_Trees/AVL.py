class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.right = right
        self.left = left

    def __str__(self):
        return self.value

    def insert(self):
        pass

    def search(self):
        pass

    def remove(self):
        pass


if __name__ == "__main__":
    root = Node(-654621)
    root.left = Node(-299999999)
    root.right = Node(-35)
    root.left.left = Node(-4)
    root.left.right = Node(-5)
    root.right.left = Node(-25)
    root.right.right = Node(-7)
    root.right.left.left = Node(-8)
    root.right.left.right = Node(-54651)
    root.right.right.right = Node(-10)

