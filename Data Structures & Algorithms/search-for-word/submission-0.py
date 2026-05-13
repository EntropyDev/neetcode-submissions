class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m,n = len(board), len(board[0])
        visited = [[False]*n for _ in range(m)]
        def dfs(r, c, i):
            if i == len(word):
                return True
            if (r>= m or r < 0 or c >=n or c <0 or word[i] != board[r][c] or visited[r][c]):
                return False
            
            visited[r][c] = True
            res = (
                dfs(r+1,c, i+1) or
                dfs(r-1,c, i+1) or
                dfs(r,c+1, i+1) or
                dfs(r,c-1, i+1) 
            )
            visited[r][c] = False
            return res
            


        for r in range(m):
            for c in range(n):
                if dfs(r,c,0):
                    return True
        return False
