class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        res = []
        s = s.lower()
        for i in s:
            #即是字母又是数字
            if i.isalnum():
                res.append(i)
        
        l,r = 0,len(res)-1
        while l<=r:
            if res[l] == res[r]:
                r -= 1
                l += 1
            else:
                return False
        return True


