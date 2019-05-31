class Heap:
    """
    Note: https://algs4.cs.princeton.edu/24pq/Heap.java.html
    """
    heap = []

    def __init__(self, arr):
        """
        Read in a list of items
        :param arr:
        """
        pass

    def insert(self, a):
        """
        Insert an item
        :param a:
        :return:
        """
        pass

    def contains(self, a):
        """
        Does the heap contain the given item
        :param a:
        :return:
        """
        return False

    def sort(self, pq):
        """
        Sort the heap
        :param pq:
        :return:
        """
        pass

    def swim(self, pq, i, j):
        """
        Move higher parent until it has lower children or is at the root
        :param pq:
        :param i:
        :param j:
        :return:
        """
        pass

    def sink(self, pq, i, j):
        """
        Move lower parent until it has a higher parent or is at the root
        :param pq:
        :param i:
        :param j:
        :return:
        """
        pass

    def less(self, pq, i, j):
        """
        Boolean to check if i is lower than j
        :param pq:
        :param i:
        :param j:
        :return:
        """
        pass

    def exchange(self, pq, i, j):
        """
        Swap items
        :param pq:
        :param i:
        :param j:
        :return:
        """
        pass

    def remove_max(self):
        pass

    def __repr__(self):
        pass

    def __str__(self):
        pass
