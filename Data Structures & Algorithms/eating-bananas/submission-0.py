import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        n = len(piles)
        l,r = 1,max(piles) # k -> 1 to max of list

        while l<r:
            m = (l+r) // 2
            # check for k = m, if you can eat all bananas in less than h hours
            # if you can move to left half,
            # if cannot, move to right half
            # break when l=r?
            count = 0
            for val in piles:
                count += math.ceil(val / m)
            if count <= h:
                r = m
            else:
                l = m+1
        return l