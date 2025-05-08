class Solution:
    def dfs(self, source, dest, adj, memo, visited):
        key = (source, dest)
        visited.add(source)
        if key in memo:
            return memo[key]
        if source == dest:
            return 1
        for nei in adj[source]:
            if nei in visited:
                continue
            res = self.dfs(nei, dest, adj, memo, visited)
            if res is not None:
                res *= adj[source][nei]
                memo[key] = res
                return memo[key]
        return None

    def calcEquation(
        self, equations: List[List[str]], values: List[float], queries: List[List[str]]
    ) -> List[float]:
        adj = defaultdict({})
        for (a, b), val in zip(equations, values):
            adj[a][b] = val
            adj[b][a] = 1 / val
        res = []
        memo = {}
        for source, dest in queries:
            res.append(self.dfs(source, dest, adj, memo, set()))
        return res
