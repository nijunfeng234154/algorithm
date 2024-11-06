class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        l = 0.0
        r = x
        #浮点数二分要有一个代表精度的最小差值

        while r-l>1e-7:
            mid = (l+r)/2.0
            if mid*mid >= x:
                r = mid
            else:
                l = mid
         
        return int(r)