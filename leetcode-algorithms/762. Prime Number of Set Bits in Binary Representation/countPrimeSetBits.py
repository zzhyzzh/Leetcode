class Solution(object):
    def countPrimeSetBits(self, L, R):
        """
        :type L: int
        :type R: int
        :rtype: int
        """
        count = 0
        for i in range(L, R + 1):
            if str(bin(i)).count("1") in [2, 3, 5, 7, 11, 13, 17, 19]:
                count += 1

        return count

solution = Solution()
result = solution.countPrimeSetBits(6, 10)
print(result)
print(type(result))