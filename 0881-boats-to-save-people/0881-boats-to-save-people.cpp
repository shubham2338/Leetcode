class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        n=len(people)
        people.sort()
        i=0
        res=0
        j=n-1
        while i<=j:
            if people[i]+people[j]<=limit:
                i+=1
                j-=1
            else:
                j-=1
            res+=1
        return res