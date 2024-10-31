class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        m = [item for row in matrix for item in row]
        def find(target,m):
            l = 0
            r = len(m)-1
            while l < r:
                mid = (l+r) // 2
                if target < mid:
                    r = mid
                else:
                    l = mid+1
            
            return (l+1) in m
        
        return find(target,m)