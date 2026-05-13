class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        words = set(wordDict)
        res = []
        sent = []

        def dfs(i):
            if i == len(s):
                res.append(" ". join(sent))
                return
            
            for j in range(i, len(s)):
                w = s[i: j+1]
                if w in words:
                    sent.append(w)
                    dfs(j+1)
                    sent.pop()
            
        dfs(0)
        return res
