class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""
        
        # 取第一个字符串作为基准
        prefix = strs[0]
        l = 0
        
        while l < len(prefix):
            for i in range(1, len(strs)):
                if l >= len(strs[i]) or strs[i][l] != prefix[l]:
                    return prefix[:l]
            l += 1
        
        return prefix
