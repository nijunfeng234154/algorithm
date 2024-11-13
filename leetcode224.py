class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = []
        for i in range(len(s)):
            if s[i].isalnum():
                stack.append(s[i])
            elif s[i] == '(':
                stack.append(s[i])
            elif s[i] == ')':
                while stack[-1] != '(':
                    x = stack.pop()
                    if x == '-':
                        stack.append(stack.pop())
                