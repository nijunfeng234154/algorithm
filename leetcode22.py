class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        def judge_str(l):
            stack = []
            mapping = {')':'('}

            for i in l:
                if i == '(':
                    stack.append(i)
                elif i in mapping and stack and mapping[i] == stack[-1]:
                    stack.pop()
                else:
                    return False
            
            return not stack

        
        def dfs(l, n, index):
            if index == 2 * n:
                if judge_str(l):
                    res.append(l)
                return
            
            dfs(l + '(', n, index + 1)
            dfs(l + ')', n, index + 1)
        
        res = []
        dfs("", n, 0)
        return res