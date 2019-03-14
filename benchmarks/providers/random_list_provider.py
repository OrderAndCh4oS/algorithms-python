from random import randint

from script_benchmark_tools import KwargsProvider


class RandomListProvider(KwargsProvider):

    def __init__(self, n, minimum, maximum):
        self.max = maximum
        self.min = minimum
        self.arr = list(self.gen_arr(n))

    def gen_arr(self, n):
        for _ in range(n):
            yield randint(self.min, self.max)

    def get(self):
        return {'arr': self.arr}
