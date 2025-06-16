class Solution:
    def find(self, s, d, adj):
        if s == d:
            return True
        for nei in adj:
            adj[nei].remove(s)
            if self.find(nei, d, adj):
                return True
        return False

    def validPath(
        self, n: int, edges: List[List[int]], source: int, destination: int
    ) -> bool:
        adj = defaultdict(set)
        for u, v in edges:
            adj[u].add(v)
            adj[v].add(u)
        return self.find(source, destination, adj)
