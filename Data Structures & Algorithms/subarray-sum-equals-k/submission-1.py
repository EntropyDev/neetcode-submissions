class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        mp = {0:1}
        s = 0
        ans = 0
        for num in nums:
            s += num
            d = s - k
            
            ans += mp.get(d,0)
            mp[s] = 1 + mp.get(s,0)
        return ans