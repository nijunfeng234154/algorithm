class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        ls = s.strip().split()
        ls = ls[::-1]
        res = ' '.join(ls)
        return res            
            