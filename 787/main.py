class Solution:
    def findCheapestPrice(
        self, n: int, flights: List[List[int]], src: int, dst: int, k: int
    ) -> int:
        adj = defaultdict(dict)
        w = [inf] * n
        w[src] = 0
        for s, d, weight in flights:
            adj[s][d] = weight
        # weight, amount of edges, node
        heap = [(0, 0, src)]
        while heap:
            weight, edges, node = heappop(heap)
            if node == dst:
                return weight
            w[node] = weight
            for nei in adj[node]:
                nei_w = weight + adj[node][nei]
                heapppush(heap, (nei_w, edges + 1, nei_w))
        return -1
