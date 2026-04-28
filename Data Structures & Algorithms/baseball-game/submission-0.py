class Solution:
    def calPoints(self, operations: List[str]) -> int:
        st = []
        ans = 0
        for i in range(len(operations)):
            c = operations[i]
            if c == '+':
                st.append(st[-1]+st[-2])
            elif c == 'D':
                st.append(st[-1]*2)
            elif c == 'C':
                st.pop()
            else:
                st.append(int(operations[i]))

        return sum(st)