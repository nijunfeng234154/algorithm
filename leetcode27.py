class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        # 输入：nums = [3,2,2,3], val = 3
        # 输出：2, nums = [2,2,_,_]
        # 双指针，左指针维护的当前数组永远不包含val,右指针将不为val的值复制给左指针
        l = 0
        for r in range(len(nums)):
            if nums[r] != val:
                nums[l] = nums[r]
                l = l+1
        
        #最后左指针的值就是结果
        return l