# class Solution(object):
#     def exist(self, board, word):
#         """
#         :type board: List[List[str]]
#         :type word: str
#         :rtype: bool
#         """
#         if not board or not board[0]:
#             return False
        
#         n = len(board)
#         m = len(board[0])
#         bo = [[0]*m for _ in range(n)]
#         dx = [-1,1,0,0]
#         dy = [0,0,1,-1]

#         res = 0
#         def dfs(board,word,path,x,y):
#             if x >= m or y >= n or x<0 or y<0:
#                 return 
#             if path == word:
#                 res = 1
#                 return 
            
#             for i in range(len(dx)):
#                 x = x + dx[i]
#                 y = y + dy[i]
#                 if x>=0 and x<m and y>=0 and y<n and bo[x][y] == 0:
#                     path = path+board[x][y]
#                     bo[x][y] = 1
#                     dfs(board,word,path,x,y)
#                     bo[x][y] = 0
#                     path = path[:-1]
        
#         # dfs(board,word,'',0,0)
#         for i in range(n):
#             for j in range(m):
#                 dfs(board, word, '', i, j)

#         if res == 1:
#             return True
#         return False
class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        if not board or not board[0]:
            return False
        
        n = len(board)
        m = len(board[0])
        bo = [[0]*m for _ in range(n)]
        dx = [-1, 1, 0, 0]
        dy = [0, 0, 1, -1]
        
        def dfs(board, word, path, x, y):
            if path == word:
                return True
            if x < 0 or y < 0 or x >= n or y >= m or bo[x][y] == 1 or board[x][y] != word[len(path)]:
                return False
            
            bo[x][y] = 1
            path += board[x][y]
            
            for i in range(4):
                if dfs(board, word, path, x + dx[i], y + dy[i]):
                    return True
            
            bo[x][y] = 0
            
        
        for i in range(n):
            for j in range(m):
                if dfs(board, word, '', i, j):
                    return True
        
        return False