class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        def digitSquareSum(n):
            return sum([int(digit) ** 2 for digit in str(n)])
        hastSet = set()
        happy = n
        while happy not in hastSet:
            hastSet.add(happy)
            happy = digitSquareSum(happy)
        if happy == 1:
            return True
        else:
            return False

solution = Solution()
result = solution.isHappy(19)
print(result)
print(type(result))