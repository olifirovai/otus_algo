class Node:
    def __init__(self, value, root=None, left=None, right=None):
        self.root = root
        self.value = value
        self.right = right
        self.left = left

    def __str__(self):
        return self.value

    def insert(self, value):
        if self.root <= value:
            self.right = value
        else:
            self.left = value

    def search(self):
        pass

    def remove(self):
        pass


