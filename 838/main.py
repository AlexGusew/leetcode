Class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        res = ['.'] * len(dominoes)
        q = deque((idx, i) for idx, i in enumerate(dominoes) if i in "LR")
        last = None
        while q:
            idx, val = q.popleft()
            if not (0 <= idx < len(dominoes)) or res[idx] == val:
                continue
            # for r.l -> r/l
            if res[idx] != '.':
                res[idx] = '.'
                q.pop()
                continue
            res[idx] = val
            # for rl
            if last and last[1] == 'R' and val == 'L' and last[0] == idx - 1:
                q.pop()
                continue    
            q.append((idx + (1 if val == 'R' else -1), val))
            last = (idx, val)
        return "".join(res)
LR...L
  R L
rr.l
rr.l
  r
  l
rl
