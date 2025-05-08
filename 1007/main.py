from math import inf


class Solution:
    def minDominoRotations(self, tops: list[int], bottoms: list[int]) -> int:
        at = ab = bt = bb = 0
        targets = tops[0], bottoms[0]
        for top, bottom in zip(tops, bottoms):
            if top not in targets and bottom not in targets:
                return -1
            at += top == tops[0]
            ab += bottom == tops[0]
            bt += top == bottoms[0]
            bb += bottom == bottoms[0]

        return min(
            # *(at, ab) if at + ab == len(tops) else inf,
            # *(bt, bb) if bt + bb == len(tops) else inf,
        )


# 1,2,1,2,3
# 3,3,3,3,2
#
# at = 2
# ab = 0
# bt = 1
# bb = 4
# 1: 2
# 3: 5
