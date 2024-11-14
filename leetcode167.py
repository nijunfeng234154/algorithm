class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        #二分
        
        def find_x(numbers,tar,l):
            r = len(numbers)-1
            while l<r:
                mid = (l+r)//2
                if numbers[mid] >= tar:
                    r = mid
                else:
                    l = mid+1
            
            return r

        for i in range(len(numbers)):
            x = find_x(numbers,target-numbers[i],i+1)
            if numbers[x] == target-numbers[i]:
                return [i+1,x+1]