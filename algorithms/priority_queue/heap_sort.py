import random

from algorithms.priority_queue.priority_queue import PriorityQueue


def heap_sort(priority_queue):
    arr = []
    for _ in range(priority_queue.size()):
        arr.insert(0, priority_queue.delete_max())

    return arr


if __name__ == '__main__':
    pq = PriorityQueue()

    arr = list(range(100))
    random.shuffle(arr)

    for x in arr:
        pq.insert(x)

    print(heap_sort(pq))
