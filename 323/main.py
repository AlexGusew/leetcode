class UF:
    def __init__(self, n):
        self.roots = list(range(n))
        self.ranks = [0] * n
        self.count = n

    def find(self, a):
        if self.roots[a] != a:
            self.roots[a] = self.find(self.roots[a])
        return self.roots[a]

    def union(self, a, b):
        a = self.find(a)
        b = self.find(b)
        if a == b:
            return
        self.count -= 1
        if self.ranks[a] < self.ranks[b]:
            a, b = b, a
        self.roots[b] = a
        self.ranks[a] += self.ranks[a] == self.ranks[b]


class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        uf = UF(n)
        for a, b in edges:
            uf.union(a, b)
        return uf.count
