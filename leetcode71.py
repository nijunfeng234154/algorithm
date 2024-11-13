class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        if not path:
            return ''
        names = path.split('/')
        #这样分隔后names里可能有空值
        #空值不能入栈
        stack = []
        for name in names:
            if name == '..':
                stack.pop()
            elif name != '.' and name:
                stack.append(name)
        
        return '/'+'/'.join(stack)
    
sol = Solution()

print(sol.simplifyPath("/home//foo/"))
print(sol.simplifyPath("/home/user/Documents/../Pictures"))
print(sol.simplifyPath("/.../a/../b/c/../d/./"))