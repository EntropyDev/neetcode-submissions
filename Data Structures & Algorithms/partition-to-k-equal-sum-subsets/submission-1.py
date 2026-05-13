class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        s = sum(nums) // k
        sides = [0]*k
        nums.sort(reverse = True)
        
        def dfs(i):
            if i == len(nums):
                for j in range(k):
                    if sides[j] != s:
                        return False
                return True
            
            for side in range(k):
                if sides[side] + nums[i] <= s:
                    sides[side] += nums[i]
                    if dfs(i+1):
                        return True
                    sides[side] -= nums[i]
                if sides[side] == 0:
                    break
            return False

        return dfs(0)
