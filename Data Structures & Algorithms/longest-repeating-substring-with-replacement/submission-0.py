class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        mp = {}
        l = 0
        ans = 0
        maxf = 0

        for r in range(len(s)):
            mp[s[r]] = 1 + mp.get(s[r], 0)
            maxf = max(maxf, mp[s[r]])
            while r-l+1 - maxf > k:
                mp[s[l]] -= 1
                l += 1
            ans = max(ans, r-l+1)
        return ans