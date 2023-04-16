class Solution:
    def numWays(self, words: List[str], t: str) -> int:
        @lru_cache(None)
        def dfs(i: int, j: int) -> int:
            if j >= len(t):
                return 1
            k = len(cnt) - len(t) + j + 1
            return sum(cnt[k][t[j]] * dfs(k + 1, j + 1) for k in range(i, k)) % 1000000007
        cnt = [collections.Counter(w[i] for w in words) for i in range(len(words[0]))]
        return dfs(0, 0)