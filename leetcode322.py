class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        #初始化都是初始化为总价值+1
        f = [1e8]*(amount+1)
        
        f[0] = 0
        #f[i]表示从0到i这个硬币这些位置所有选择满足amount集合的最小值
        #完全背包，把问题看成每个硬币价值为1，体积为金额
        for i in coins:
            for j in range(i,amount+1):
                f[j] = min(f[j],f[j-i]+1)
        
        if f[amount] == 1e8:
            return -1
        
        return f[amount]
