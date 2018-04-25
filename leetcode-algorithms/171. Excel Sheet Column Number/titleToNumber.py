class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = s[::-1]
        order = 0
        digit = 0
        for letter in s:
            order += pow(26, digit) * (ord(letter) - 65 + 1)
            digit += 1

        return order

solution = Solution()
result = solution.titleToNumber("BA")
print(result)