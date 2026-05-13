class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]

        def helper(numbers):
            if not numbers:
                return 0
            if len(numbers) == 1:
                return numbers[0]
            dp = [0]*len(numbers)
            dp[0] = numbers[0]
            dp[1] = max(numbers[0], numbers[1])

            for i in range(2, len(numbers)):
                dp[i] = max(dp[i-1], numbers[i]+ dp[i-2])
            return dp[-1]
        return max(helper(nums[1:]), helper(nums[:-1]))
        
