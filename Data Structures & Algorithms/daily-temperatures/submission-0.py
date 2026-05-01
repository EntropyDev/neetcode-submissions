class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        st = []
        # monotonicaly decreasing stack with (t, i).
        # [22,21,20]
        # for pos i, find next greater elm, res add (elmi - i).
        res = [0]*len(temperatures)
        for i in range(len(temperatures)):
            while st and temperatures[i] > temperatures[st[-1]]:
                j = st.pop()
                res[j] = i-j
            st.append(i)
        return res
