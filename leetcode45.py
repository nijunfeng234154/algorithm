class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = []
        def dfs(nums,path,cnt):
            if path == len(nums)-1:
                res.append(cnt)
                return 
            if path >= len(nums):
                return 

            #搜索每一步要跳多少个位置
            for i in range(1,nums[path]+1):
                dfs(nums,path+i,cnt+1)

        dfs(nums,0,0) 
        return min(res) 

sol = Solution()
print(sol.jump([2,3,1,1,4]))     
print(sol.jump([2,3,0,1,4]))     

                
