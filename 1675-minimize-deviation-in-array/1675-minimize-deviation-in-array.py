class Solution:
    def minimumDeviation(self, nums: List[int]) -> int:
        h = list(set(-(x * 2 if x & 1 else x) for x in nums))
        heapq.heapify(h)
        ma, mi = -h[0], -max(h)
        ans = ma - mi
        while h[0] % 2 == 0:
            x = heapq.heappop(h) // 2
            heapq.heappush(h, x)
            ma, mi = -h[0], min(mi, -x)
            ans = min(ans, ma - mi)
        return ans