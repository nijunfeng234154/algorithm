class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        l = 0
        r = len(nums)-1
        pos = 0

        if not nums:
            return -1
        
        # 第一次二分找旋转点
        while l < r:
            mid = (l + r) // 2
            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid
        
        rot = l
        l, r = 0, len(nums) - 1

        #第二次二分做坐标映射，映射为排序好的正常数组二分
        while l<r:
            mid = (l+r)//2
            #映射的中点坐标
            pos = (mid+rot)%len(nums)
            if nums[pos] >= target:
                r = mid
            else:
                l = mid + 1

        if nums[(r+rot)%len(nums)] == target:
            return (r+rot)%len(nums)
        else:
            return -1
