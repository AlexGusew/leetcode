class Solution:
    def dfs(self, node, group, visited, adj):
        if node in visited:
            return
        group.append(node)
        visited.add(node)
        for nei in adj:
            self.dfs(nei, group, visited, adj)
        return group

    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        groups = []
        visited = set()
        adj = defaultdict(list)
        for a, b in pairs:
            adj[a].append(b)
            adj[b].append(a)
        for node in range(len(s)):
            if node not in visited:
                groups.append(self.dfs(node, [], visited, adj))

        res = [None] * len(s)
        for group in groups:
            group.sort(key=lambda idx: s[idx])
            idxs = list(sorted(group))
            for idx, target in zip(idxs, group):
                res[idx] = s[target]
        return "".join(res)
