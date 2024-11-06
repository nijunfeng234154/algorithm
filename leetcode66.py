class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        x = ''.join(str(digit) for digit in digits)
        return [int(i) for i in str(int(x)+1)] 