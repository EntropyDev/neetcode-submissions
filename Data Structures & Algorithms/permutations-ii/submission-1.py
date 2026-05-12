class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res=[]
        def dfs(perm, visit):
            if len(perm) == len(nums):
                res.append(perm.copy())
                return
            for i in range(len(nums)):
                if visit[i]:
                    continue
                if i and nums[i] == nums[i-1] and not visit[i-1]:
                    continue

                perm.append(nums[i])
                visit[i]= True
                dfs(perm, visit)
                perm.pop()
                visit[i]=False

        nums.sort()
        dfs([], [False]*len(nums))
        return res