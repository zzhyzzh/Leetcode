class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        maxProfit = 0
        if prices:
            price = prices[0]
        for i in range(1, len(prices)):
            if prices[i] >= price:
                maxProfit += prices[i] - price
            price = prices[i]
        return maxProfit

solution = Solution()
result = solution.maxProfit([1,2,4])
print(result)