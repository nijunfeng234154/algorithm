class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        if not nums:
            return []
        if len(nums)==1:
            return [str(nums[0])]
        
        res = []
        l = 0
        for i in range(1,len(nums)):
            if nums[i]-nums[i-1]>1:
                res.append([nums[l],nums[i-1]])
                l = i
        
        res.append([nums[l],nums[-1]])
        
        for i in range(len(res)):
            if res[i][0]!=res[i][1]:
                res[i] = str(res[i][0])+'->'+str(res[i][1])
            else:
                res[i] = str(res[i][0])    

        return res 