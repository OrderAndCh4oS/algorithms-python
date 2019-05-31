class PriorityQueue:
    """
    Note: https://algs4.cs.princeton.edu/24pq/
    Note: https://algs4.cs.princeton.edu/24pq/MaxPQ.java.html
    """
    priority_queue = [None]
    n = 0

    def insert(self, a):
        self.priority_queue.append(a)
        if self.is_empty():
            return
        self.swim(self.size())
        self.n += 1
        assert self.is_max_heap(1)

    def swim(self, key):
        while key > 1 and self.less(key / 2, key):
            self.exchange(key, key / 2)
            key = key / 2

    def sink(self, key):
        while key * 2 <= self.size():
            print(self.priority_queue)
            j = key * 2
            if j < self.size() and self.less(j, j + 1):
                j += 1
            if not self.less(key, j):
                print('Break')
                print(self.priority_queue)
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
        return len(self.priority_queue) == 1

    def size(self):
        return self.n

    def __repr__(self):
        return str(self.priority_queue)


if __name__ == '__main__':
    pq = PriorityQueue()

    pq.insert(4)
    pq.insert(2)
    pq.insert(16)
    pq.insert(7)
    pq.insert(11)
    pq.insert(15)
    pq.insert(9)
    pq.insert(14)
    pq.insert(12)
    pq.insert(5)
    pq.insert(3)
    pq.insert(13)
    pq.insert(6)
    pq.insert(8)
    pq.insert(17)
    pq.insert(1)
    pq.insert(10)

    print('Result')
    print(pq)
    for _ in range(17):
        print(pq)
        print(pq.delete_max())
        print('Result')
        print(pq)
        print('________')
