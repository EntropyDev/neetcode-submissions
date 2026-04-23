class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix = [1]*(n+1)
        postfix = [1]*(n+1)

        for i in range(1,n+1):
            prefix[i] = prefix[i-1]*nums[i-1]
        
        for i in range(n,1,-1):
            postfix[i-1] = postfix[i] * nums[i-1]
        
        res = []
        for i in range(n):
            res.append(prefix[i]*postfix[i+1])
        return res

            #     [1, 2, 4, 6]
            # pr. [1, 1, 2, 8, 48]
            # ps. [48, 48, 24, 6, 1]