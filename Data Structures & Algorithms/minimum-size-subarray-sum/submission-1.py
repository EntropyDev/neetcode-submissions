class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        res = float('inf')

        l = r = 0
        s = 0
        while r < len(nums):
            s += nums[r]
            while l <= r and s >= target:
                res = min(res, r-l+1)
                s -= nums[l]
                l += 1
            r += 1
            

        return 0 if res == float('inf') else res