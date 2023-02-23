class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        mp=[]
        mc=[(c,p) for c,p in zip(capital,profits)]
        heapq.heapify(mc)
        while k:
            while mc and mc[0][0]<=w:
                c,p=heapq.heappop(mc)
                heapq.heappush(mp,-p)
            if not mp:
                break
            w+=-(heapq.heappop(mp))
            k-=1
        return w
        