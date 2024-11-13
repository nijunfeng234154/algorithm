class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        if not obstacleGrid:
            return 0
        
        #初始化dp数组
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        
        #起点或终点有障碍物，直接返回0
        if obstacleGrid[0][0] == 1 or obstacleGrid[m-1][n-1] == 1:
            return 0
        dp = [[0 for _ in range(n)] for _ in range(m)]

        dp[0][0] = 1
        
        #初始化dp数组，处理第一列
        for i in range(1, m):
            if obstacleGrid[i][0] == 1 or dp[i - 1][0] == 0:
                dp[i][0] = 0
            else:
                dp[i][0] = 1
                
        #处理第一行        
        for j in range(1, n):
            if obstacleGrid[0][j] == 1 or dp[0][j - 1] == 0:
                dp[0][j] = 0
            else:
                dp[0][j] = 1

        for i in range(1,m):
            for j in range(1,n):
                if obstacleGrid[i][j] == 1:
                    dp[i][j] = 0
                else:
                    dp[i][j] = dp[i][j-1]+dp[i-1][j]

        return dp[m-1][n-1]