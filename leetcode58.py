class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        # return len(s.strip().split()[-1])
        l = len(s.rstrip())-1
        cnt = 0
        while l >= 0:
            if s[l].isalnum():
                cnt += 1
            if s[l] == ' ' and l < len(s)-1:
                break

            l -= 1
        
        return cnt
        