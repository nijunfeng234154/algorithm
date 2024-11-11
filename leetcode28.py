# class Solution(object):
#     def strStr(self, haystack, needle):
#         """
#         :type haystack: str
#         :type needle: str
#         :rtype: int
#         """
#         if not needle:
#             return 0
        

#         j = 0
#         for i in range(len(haystack)):
#             if haystack[i] == needle[j]:
#                 j += 1
#             else:
#                 #i回退位置
#                 i = i-j
#                 j = 0
#             if j == len(needle)-1:
#                 return i-j+1
        
#         return -1
class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if not needle:
            return 0
        
        j = 0
        i = 0
        while i < len(haystack):
            if haystack[i] == needle[j]:
                j += 1
                if j == len(needle):
                    return i - j + 1
            else:
                i = i - j
                j = 0
            i += 1
        
        return -1

# 测试代码
sol = Solution()
print(sol.strStr("hello", "ll"))  # 输出: 2
print(sol.strStr("aaaaa", "bba"))  # 输出: -1
print(sol.strStr("", ""))  # 输出: 0
print(sol.strStr("a", ""))  # 输出: 0
print(sol.strStr("mississippi", "issip"))  # 输出: 4
