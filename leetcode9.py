class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        x1 = x
        y = 0
        while x1>0:
            y = y*10+x1%10
            x1 = x1/10
        
        return x==y