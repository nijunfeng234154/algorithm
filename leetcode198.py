class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        
        #注意动态规划的初始化
        f = [0]*len(nums)
        f[0] = nums[0]
        f[1] = max(nums[0],nums[1])
        
        #f[i]表示当前位置之前能够偷到的钱的集合的最大值
        for i in range(2,len(nums)):
            f[i] = max(f[i-1],f[i-2]+nums[i])

        #返回最后一个位置之前能够偷到钱的集合的最大值，就是答案
        return max(f[-1])