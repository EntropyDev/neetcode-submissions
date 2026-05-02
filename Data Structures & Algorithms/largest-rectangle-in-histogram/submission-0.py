class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        leftmost = [-1]*n
        rightmost= [n]*n
        res = 0
        
        st = []
        for i in range(n):
            while st and heights[st[-1]] >= heights[i]:
                st.pop()
            if st:
                leftmost[i] = st[-1]
            st.append(i)
        
        st = []
        for i in range(n-1, -1, -1):
            while st and heights[st[-1]] >= heights[i]:
                st.pop()
            if st:
                rightmost[i] = st[-1]
            st.append(i)
        
        for i in range(n):
            leftmost[i] += 1
            rightmost[i] -= 1
            res = max(res, heights[i]*(rightmost[i] - leftmost[i] + 1))

        return res