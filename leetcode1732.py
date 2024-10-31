class Solution(object):
    def largestAltitude(self, gain):
        """
        :type gain: List[int]
        :rtype: int
        """
        s = [0]*(len(gain)+5)
        s[0] = gain[0]
        for i in range(1,len(gain)):
            s[i] = s[i-1] + gain[i] 

        return max(s)