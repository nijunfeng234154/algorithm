class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])

        f = [[0 for _ in range(n)] for _ in range(m)]

        if m == 1 and n == 1:
            return grid[0][0]
        elif m==1 and n==0:
            return grid[0]

        #注意初始化/特殊边界条件
        for i in range(m):
            for j in range(n):
                f[i][j] = grid[i][j]
                if j == 0 and i>0:
                    f[i][j] += f[i-1][j]
                elif i == 0 and j>0:
                    f[i][j] += f[i][j-1]
                else:
                    f[i][j] += min(f[i-1][j],f[i][j-1])
        
        return f[m-1][n-1]