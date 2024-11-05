class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return -1
        l = 0
        r = len(nums)-1
        rot = 0

        # 第一次二分找旋转点
        while l < r:
            mid = (l + r) // 2
            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid
        
        rot = l
        
        return nums[rot%len(nums)]