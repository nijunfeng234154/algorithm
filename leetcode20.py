class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        mapping = {')':'(',']':'[','}':'{'}
        for i in s:
            if i == '(' or i == '[' or i == '{':
                stack.push(i)
            elif stack[-1] == mapping[i]:
                stack.pop()
            else:
                return False
        
        return not stack