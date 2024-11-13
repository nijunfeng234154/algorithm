class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = []
        #先把总体思路想清楚再写
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
                