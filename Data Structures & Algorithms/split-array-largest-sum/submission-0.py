class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:

        def canSplit(largest):
            count = 1
            cur = 0
            for num in nums:
                cur += num
                if cur > largest:
                    count += 1
                    if count > k:
                        return False
                    cur = num
            return True


        l,r = max(nums), sum(nums)
        res = r
        while l<=r:
            m = (l + r) // 2

            if canSplit(m):
                res = m
                r = m-1
            else:
                l = m+1
        return res

