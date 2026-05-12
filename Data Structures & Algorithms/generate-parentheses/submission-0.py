class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        st = []

        def dfs(opn, cls):
            if opn == cls == n:
                res.append("".join(st))
                return
            if opn < n:
                st.append("(")
                dfs(opn+1, cls)
                st.pop()
            if cls < opn:
                st.append(")")
                dfs(opn, cls+1)
                st.pop()
                
        dfs(0, 0)
        return res