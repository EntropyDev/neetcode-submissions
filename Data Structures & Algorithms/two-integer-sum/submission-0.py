class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ans = []
        # O(n2)
        # O(nlogn) -> sort with indices pair. ?Still O(n2)
        # O(n) -> use set/map to check if val already seen.
        mp = {}
        for i in range(len(nums)):
            if target-nums[i] in mp:
                return [mp[target - nums[i]], i]
            mp[nums[i]] = i

