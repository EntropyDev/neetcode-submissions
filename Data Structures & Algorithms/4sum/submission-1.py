class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res = []
        n = len(nums)

        for k in range(n):
            if k>0 and nums[k] == nums[k-1]:
                continue
            for i in range(k+1,n):
                if i>k+1 and nums[i] == nums[i-1]:
                    continue
                l = i+1
                r = n-1
                while l < r:
                    s = nums[l] + nums[r] + nums[i] + nums[k]
                    if s > target:
                        r -= 1
                    elif s < target:
                        l += 1
                    else:
                        res.append([nums[k],nums[i],nums[l],nums[r]])
                        l += 1
                        r -= 1
                        while l<r and nums[l] == nums[l-1]:
                            l+=1


        return res