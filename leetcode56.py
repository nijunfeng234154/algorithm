class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        #每道题都要注意细节和边界条件
        if not intervals:
            return []
        
        intervals.sort()
        my_seq = intervals[0]
        res = [] 
        for seq in intervals:
            if my_seq[1] < seq[0]:
                res.append(my_seq)
                my_seq = seq
            else:
                my_seq[1] = max(my_seq[1],seq[1])


        res.append(my_seq)
        return res
