class UF:
    def __init__(self, weights):
        self.roots = list(range(len(weights)))
        self.ranks = [0] * len(weights)
        self.weights = weights

    def find(self, a):
        if a != self.roots[a]:
            self.roots[a] = self.find(self.roots[a])
        return self.roots[a]

    def union(self, a, b, weight):
        a = self.find(a)
        b = self.find(b)
        wa = self.weights[a]
        wb = self.weights[b]
        if a == b or min(wa, wb) + weight > max(wa, wb):
            return
        if self.ranks[a] < self.ranks[b]:
            a, b = b, a
        self.ranks[a] += self.ranks[a] == self.ranks[b]
        self.roots[b] = a
        self.weights[a] += weight
        self.weights[b] = 0


class Solution:
    def minCostToSupplyWater(
        self, n: int, wells: list[int], pipes: list[list[int]]
    ) -> int:
        adj = defaultdict(dict)
        heap = [(0, 0)]
        total = 0
        visited = set()
        for idx, weight in enumerate(wells):
            adj[0][idx + 1] = weight
            adj[idx + 1][0] = weight
        for a, b, weight in pipes:
            adj[a][b] = weight
            adj[b][a] = weight
        while heap:
            w, node = heappop(heap)
            if node in visited:
                continue
            total += w
            visited.add(node)
            for nei in adj[node]:
                heappush((adj[node][nei], nei))
        return total


"""
1. uf
2. store edges in heap
3. store cost for each component
4. When union, decrease comp cost.
Union when result is smaller than current
"""
