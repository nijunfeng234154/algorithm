class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        m = len(triangle)
        n = len(triangle[-1])
        
        f = [[0 for _ in range(n)] for _ in range(m)]

        for i in range(m):
            for j in range(n):
                if j>i:
                    f[i][j] = 1000
                else:
                    f[i][j] = triangle[i][j]
        
        for i in range(1,m):
            for j in range(n):
                if j == 0:
                    f[i][j] += f[i-1][j]
                elif j <= i:
                    f[i][j] += min(f[i-1][j], f[i-1][j-1])
        
        
        return min(f[-1])