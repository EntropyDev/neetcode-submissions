class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        n = len(weights)
        l,r = max(weights), sum(weights)

        while l<r:
            m = (l+r) // 2
            count = 1
            cur = 0
            for w in weights:
                if cur+w > m:
                    count += 1
                    cur = w
                else:
                    cur += w
       
            if count <= days:
                r = m
            else:
                l = m+1
            
        return l