class Solution:
    def lengthAfterTransformations(self, s: str, t: int) -> int:
        counter = Counter(s)
        MOD = 10**9 + 7
        for _ in range(t):
            c = Counter()
            for char in counter:
                if char == "z":
                    c["a"] = (c["a"] + counter[char]) % MOD
                    c["b"] = (c["b"] + counter[char]) % MOD
                else:
                    c[chr(ord(char) + 1)] = (
                        counter[char] + c[chr(ord(char) + 1)]
                    ) % MOD
            counter = c
        return sum(counter.values()) % MOD
