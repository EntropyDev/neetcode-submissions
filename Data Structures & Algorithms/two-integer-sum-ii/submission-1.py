class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l,r = 0, len(numbers)-1
        res = []
        while l < r:
            s = numbers[l] + numbers[r]
            if s < target:
                l+= 1
            elif s > target:
                r -= 1
            else:
                res = [l+1, r+1]
                break

        return res
