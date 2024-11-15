class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        #双指针 二重循环 O(n^2)
        if not nums or len(nums)<3:
            return []
        res = []
        nums = sorted(nums)
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue  # 跳过重复元素
            z = nums[i]
            l,r = i+1,len(nums)-1
            while l<r:
                if nums[l]+nums[r] == -z:
                    res.append([nums[i],nums[l],nums[r]])
                    while l < r and nums[l] == nums[l + 1]:
                        l += 1  # 跳过重复元素
                    while l < r and nums[r] == nums[r - 1]:
                        r -= 1  # 跳过重复元素
                    l += 1
                    r -= 1
                elif nums[l]+nums[r] > -z:
                    r -= 1
                elif nums[l]+nums[r] < -z:
                    l += 1
        
        return res