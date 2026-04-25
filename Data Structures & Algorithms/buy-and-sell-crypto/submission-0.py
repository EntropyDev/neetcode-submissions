class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        curMin = prices[0]
        res = 0
        for i in range(1,len(prices)):
            if curMin < prices[i]:
                pr = prices[i] - curMin
                res = max(pr,res)
            else:
                curMin = min(curMin, prices[i])
        return res