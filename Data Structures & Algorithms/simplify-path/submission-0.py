class Solution:
    def simplifyPath(self, path: str) -> str:
        arr = path.split('/')
        st = []
        for cur in arr:
            if cur == "..":
                if st:
                    st.pop()
            elif cur != "" and cur !=".":
                st.append(cur)

        return "/" + "/".join(st)