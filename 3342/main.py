class Solution:
    DIRECTIONS = ((0, 1), (0, -1), (1, 0), (-1, 0))

    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        m, n = len(moveTime), len(moveTime[0])
        times = [inf] * m * n
        times[0] = 0
        heap = [(0, 0, True)]  # time, coord, is odd
        while heap:
            time, coord, odd = heappop(heap)
            if coord == m * n - 1:
                return time
            times[coord] = time
            for di, dj in self.DIRECTIONS:
                row, col = divmod(coord, n)
                i, j = row + di, col + dj
                if not (0 <= i < m and 0 <= j < n):
                    continue
                next_coord = i * n + j
                next_time = max(time, moveTime[i][j]) + (1 if odd else 2)
                if next_time < times[next_coord]:
                    times[next_coord] = next_time
                    heappush(heap, (next_time, next_coord, not odd))
