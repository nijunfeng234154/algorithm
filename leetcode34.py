class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        l,r = 0,len(nums)-1
        while l<r:
            mid= (l+r+1)//2
            if nums[mid]>target:
                r = mid-1
            else:
                l = mid

        resr = r
        l,r = 0,len(nums)-1
        while l<r:
            mid= (l+r)//2
            if nums[mid]<target:
                l = mid+1
            else:
                r = mid
        resl = l
        
        if resl<0 or resl>len(nums) or resr<0 or resr>=len(nums):
            print([-1,-1])
        elif (nums[resl]!=target and nums[resr]!=target):
            print([-1,-1])
        else:
            print([resl,resr])
def test_searchRange():
    sol = Solution()
    
    # Test case 1: target is in the middle
    nums = [5, 7, 7, 8, 8, 10]
    target = 8
    sol.searchRange(nums, target)
    
    # Test case 2: target is at the beginning
    nums = [5, 7, 7, 8, 8, 10]
    target = 5
    sol.searchRange(nums, target)
    
    # Test case 3: target is at the end
    nums = [5, 7, 7, 8, 8, 10]
    target = 10
    sol.searchRange(nums, target)
    
    # Test case 4: target is not in the list
    nums = [5, 7, 7, 8, 8, 10]
    target = 6
    sol.searchRange(nums, target)
    
    # Test case 5: empty list
    nums = []
    target = 0
    sol.searchRange(nums, target) 
    # Test case 6: list with one element, target is present
    nums = [1]
    target = 1
    assert sol.searchRange(nums, target) == [0, 0], f"Test case 6 failed: {sol.searchRange(nums, target)}"
    
    # Test case 7: list with one element, target is not present
    nums = [1]
    target = 0
    assert sol.searchRange(nums, target) == [-1, -1], f"Test case 7 failed: {sol.searchRange(nums, target)}"
    
    print("All test cases passed!")

test_searchRange()