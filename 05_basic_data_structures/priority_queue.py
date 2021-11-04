class PriorityQueue:
    def __init__(self):
        self.queue = []

    def __str__(self):
        return ' '.join([str(i) for i in self.queue])

    def is_empty(self):
        return len(self.queue) == 0

    def enqueue(self, data):
        self.queue.append(data)

    def dequeue(self):
        if not self.is_empty():
            high_priority = 0
            for i in range(len(self.queue)):
                if self.queue[i] > self.queue[high_priority]:
                    high_priority = i
            item = self.queue[high_priority]
            del self.queue[high_priority]
            return item


if __name__ == '__main__':
    my_queue = PriorityQueue()
    my_queue.enqueue(12)
    my_queue.enqueue(1)
    my_queue.enqueue(14)
    my_queue.enqueue(7)
    print(my_queue)
    while not my_queue.is_empty():
        print(my_queue.dequeue())
