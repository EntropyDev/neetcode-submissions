class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0
        # k keeps track of elements which are not val
        # loop through array
        # if cur elm is not val, put it in kth pos, increase k by 1.
        # basically go through array collect all the non val elm and inc k.
        for n in nums:
            if n != val:
                nums[k] = n
                k += 1
        return k
            