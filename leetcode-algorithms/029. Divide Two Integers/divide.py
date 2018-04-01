INT_MAX = 2147483647

class Solution:
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        if divisor == 0:
            return INT_MAX
        isPositive = (dividend > 0) == (divisor > 0)
        result = 0
        dividend, divisor = abs(dividend), abs(divisor)
        while dividend >= divisor:
            temp, i = divisor, 1
            while dividend >= temp:
                dividend -= temp
                result += i
                temp <<= 1
                i <<= 1
        result = 0 - result if not isPositive else result
        return min(result, INT_MAX)

solution = Solution()
result = solution.divide(-2147483648, -1)
print(result)
print(type(result))