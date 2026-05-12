class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []

        def dfs(i, subset, total):
            if total == target:
                res.append(subset.copy())
                return
            if i >= len(candidates) or total > target:
                return

            # ✅ PICK current element
            subset.append(candidates[i])
            dfs(i + 1, subset, total + candidates[i])
            subset.pop()

            # ✅ SKIP all duplicates of current element
            j = i
            while j + 1 < len(candidates) and candidates[j] == candidates[j + 1]:
                j += 1

            dfs(j + 1, subset, total)
        
        dfs(0, [], 0)

        return res