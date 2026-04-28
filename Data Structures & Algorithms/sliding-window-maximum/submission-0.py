class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        mxHeap = []
        for i in range(len(nums)):
            heapq.heappush(mxHeap, (-nums[i], i))
            if i >= k-1:
                while mxHeap[0][1] <= i-k:
                    heapq.heappop(mxHeap)
                res.append(-mxHeap[0][0])
        return res