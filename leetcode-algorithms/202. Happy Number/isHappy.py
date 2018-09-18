class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        def digitSquareSum(n):
            return sum([int(digit) ** 2 for digit in str(n)])
        slow = fast = n
        while True:
            slow = digitSquareSum(slow)
            fast = digitSquareSum(digitSquareSum(fast))
            if slow == fast:
                break
        if slow == 1:
            return True
        else:
            return False

solution = Solution()
result = solution.isHappy(19)
print(result)
print(type(result))