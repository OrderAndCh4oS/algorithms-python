
class UnionFind:
    def __init__(self, n):
        self._ids = [i for i in range(n)]
        self._count = n

    def get_count(self):
        return self._count

    def connected(self, p, q):
        return self.find(p) == self.find(q)

    def find(self, p):
        return self._ids[p]

    def union(self, p, q):
        p_id = self.find(p)
        q_id = self.find(q)
        if p_id == q_id:
            return
        for i in range(len(self._ids)):
            if self._ids[i] == p_id:
                self._ids[i] = q_id
        self._count -= 1


if __name__ == '__main__':
    n = int(input())
    union_find = UnionFind(n)
    while True:
        data = input()
        if data == '':
            break
        data = data.split(' ')
        p, q = int(data[0]), int(data[1])
        if union_find.connected(p, q):
            continue
        union_find.union(p, q)
        print(p, q)

    print("Components count: ", union_find.get_count())
