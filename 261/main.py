class Solution:
    def dfs(self, node, visited, adj):
        q = deque([node])
        while q:
            v = q.popleft()
            if visited[v]:
                return False
            visited[v] = True
            for nei in adj[v]:
                adj[nei].remove(v)
                q.append(nei)
        return True

    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj = defaultdict(set)
        for a, b in edges:
            adj[a].add(b)
            adj[b].add(a)
        visited = [False] * n
        if not self.dfs(0, visited, adj):
            return False
        return all(visited)
