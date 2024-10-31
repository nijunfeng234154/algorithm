class Solution(object):
    def removeStars(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        for i in s:
            if i != '*':
                stack.append(i)
            elif len(stack)>0 and i == '*':
                stack.pop()
            else:
                stack = []
        
        return ''.join(stack)
        