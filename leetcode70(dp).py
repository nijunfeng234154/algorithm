class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 0
        if n == 1:
            return 1
        elif n == 2:
            return 2
        else:
            f = [0]*(n+5)
            f[0] = 0
            f[1] = 1
            f[2] = 2

            for i in range(3,n+1):
                f[i] = f[i-1]+f[i-2]
            
            return f[n]