class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
       
        s = set(nums)
        res = 0
        
        for num in s:
            if num-1 not in s:
                length = 1
                while num+length in s:
                    length += 1
                res = max(res,length)
        
        return res

        # if not nums:
        #     return 0
        # res = 0
        # nums.sort()

        # curr, streak = nums[0], 0
        # i = 0
        # while i<len(nums):
        #     if curr != nums[i]:
        #         curr = nums[i]
        #         streak = 0
        #     while i < len(nums) and nums[i] == curr:
        #         i += 1
        #     streak += 1
        #     curr += 1
        #     res = max(res, streak)

        # return res