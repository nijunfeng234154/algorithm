class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        f = [10000]*(len(coins)+5)
        #f[i]表示从0到i这个硬币这些位置所有选择满足amount集合的最小值
        summ = 0
        for i in range(len(coins)):
            if summ-coins[i] == amount:
                f[i] = f[i-1]+1
            else:
                summ += coins[i]
            