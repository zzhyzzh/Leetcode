class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        isPositive = -1
        if x > 0:
            isPositive = 1
        x = abs(x)
        numberStr = str(x)
        numberStr = numberStr[::-1]
        number = int(numberStr) * isPositive

        return number if number.bit_length() <32 else 0


solution = Solution()
l1 = solution.reverse(1534236469)
print(l1)
print(type(l1))
