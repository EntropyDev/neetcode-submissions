class Solution:
    def isValid(self, s: str) -> bool:
        st = []
        for c in s:
            if c in ('(','{','['):
                st.append(c)
                continue
            if not st:
                return False
            if c == ')' and st[-1] != '(':
                return False
            if c == '}' and st[-1] != '{':
                return False
            if c == ']' and st[-1] != '[':
                return False
            st.pop()
        return len(st) == 0

