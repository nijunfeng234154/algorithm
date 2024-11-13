class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        #dfs方法 超时
        #规定方向
        dx = [0,1]
        dy = [1,0]
        if not obstacleGrid:
            return 0
        global cnt
        cnt = 0 
        def dfs(obstacleGrid,x,y):
            global cnt
            m = len(obstacleGrid)
            n = len(obstacleGrid[0])
            if obstacleGrid[y][x]==1:
                return 
            if x == n-1 and y == m-1:
                cnt+=1
                return 

            for i in range(len(dx)):
                if (x+dx[i])<n and (y+dy[i])<m and obstacleGrid[y+dy[i]][x+dx[i]]!=1:
                    dfs(obstacleGrid,x+dx[i],y+dy[i])
            
        dfs(obstacleGrid,0,0)
        return cnt