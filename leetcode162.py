class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def find(nums):
            l = 0
            r = len(nums) - 1
            while l < r:
                mid = (l + r) // 2
                if nums[mid] > nums[mid + 1]:
                    r = mid
                else:
                    l = mid + 1
            return l

        return find(nums)