class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        intervals.append(newInterval)
        def hebing(intervals):
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
        
        return hebing(intervals)