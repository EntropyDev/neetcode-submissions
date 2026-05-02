class Solution:
    def decodeString(self, s: str) -> str:
        res = ""
        st = []

        for c in s:
            if c != "]":
                st.append(c)
            else:
                t = ""
                while st[-1] != "[":
                    t = st.pop() + t
                st.pop()
                cnt = ""
                while st and st[-1].isdigit():
                    cnt = st.pop() + cnt
                st.append(int(cnt)*t)
                
        return "".join(st)