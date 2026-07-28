class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        m, n = len(mat), len(mat[0])
        
        # Count 1s in each row and column
        row_count = [sum(row) for row in mat]
        col_count = [sum(mat[i][j] for i in range(m)) for j in range(n)]
        
        result = 0
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 1 and row_count[i] == 1 and col_count[j] == 1:
                    result += 1
        return result
