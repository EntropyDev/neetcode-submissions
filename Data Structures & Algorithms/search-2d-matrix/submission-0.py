class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m,n = len(matrix),len(matrix[0])
        l,r = 0, m-1

        while l <= r:
            mid = (l+r)//2
            if matrix[mid][0] <= target <= matrix[mid][n-1]:
                # do
                i,j = 0, n-1
                while i <= j:
                    m = (i+j)//2
                    if matrix[mid][m] == target:
                        return True
                    elif matrix[mid][m] > target:
                        j = m-1
                    else:
                        i = m+1
                break
            elif matrix[mid][0] > target:
                r = mid -1
            elif matrix[mid][n-1] < target:
                l = mid+1
        return False
            
            