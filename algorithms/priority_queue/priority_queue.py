import random


class PriorityQueue:
    """
    Note: https://algs4.cs.princeton.edu/24pq/
    Note: https://algs4.cs.princeton.edu/24pq/MaxPQ.java.html
    """
    priority_queue = [None]
    n = 0

    def insert(self, a):
        self.priority_queue.append(a)
        self.n += 1
        if self.is_empty():
            return
        self.swim(self.size())

        assert self.is_max_heap(1)

    def swim(self, key):
        while key > 1 and self.less(key / 2, key):
            self.exchange(key, key / 2)
            key = key / 2

    def sink(self, key):
        while key * 2 <= self.size():
            j = key * 2
            if j < self.size() and self.less(j, j + 1):
                j += 1
            if not self.less(key, j):
                break
            self.exchange(key, j)
            key = j

    def less(self, i, j):
        if self.priority_queue[int(i)] is None or self.priority_queue[int(j)] is None:
            return False
        return self.priority_queue[int(i)] < self.priority_queue[int(j)]

    def exchange(self, i, j):
        self.priority_queue[int(i)], self.priority_queue[int(j)] = self.priority_queue[int(j)], self.priority_queue[
            int(i)]

    def is_max_heap(self, key):
        if key > self.size():
            return True
        left = key * 2
        right = key * 2 + 1
        if left < self.size() and self.less(key, left):
            return False
        if right < self.size() and self.less(key, right):
            return False
        return self.is_max_heap(left) and self.is_max_heap(right)

    def max(self):
        return self.priority_queue[1]

    def delete_max(self):
        self.exchange(1, self.size())
        maximum = self.priority_queue.pop()
        self.n -= 1
        self.sink(1)

        assert self.is_max_heap(1)

        return maximum

    def is_empty(self):
        return self.n == 0

    def size(self):
        return self.n

    def __repr__(self):
        return str(self.priority_queue)


if __name__ == '__main__':
    pq = PriorityQueue()

    arr = list(range(18))
    random.shuffle(arr)

    for x in arr:
        pq.insert(x)
        print(pq)

    sorted_arr = []

    for _ in range(17):
        print(pq)
        maximum = pq.delete_max()
        sorted_arr.insert(0, maximum)
        print('Result')
        print(pq)
        print('________')

    print(sorted_arr)
