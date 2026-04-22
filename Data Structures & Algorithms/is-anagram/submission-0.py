class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        mp = {}
        if len(s) != len(t):
            return False
        for c in s:
            mp[c] = 1 + mp.get(c,0)
        for c in t:
            if c not in mp:
                return False
            mp[c] -= 1
            if mp[c] == 0:
                mp.pop(c)
        return len(mp) == 0