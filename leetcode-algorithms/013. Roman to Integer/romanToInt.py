import re

class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        I = ["I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]
        X = ["X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
        C = ["C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
        M = ["M", "MM", "MMM"]

        romans = [M, C, X, I]
        romanInt = 0
        for j in range(len(romans)):
            for i in range(len(romans[j]) - 1, -1, -1):
                if re.match(romans[j][i], s):
                    s = s[len(romans[j][i]):]
                    romanInt += (10 ** (3 - j)) * (i + 1)
                    break

        return romanInt

solution = Solution()
result = solution.romanToInt("DCXXI")
print(result)
print(type(result))