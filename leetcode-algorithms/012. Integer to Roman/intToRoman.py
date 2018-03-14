class Solution:
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        I = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]
        X = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
        C = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
        M = ["", "M", "MM", "MMM"]

        roman = M[int(num/1000)] + \
                C[int((num%1000)/100)] + \
                X[int((num%100)/10)] +\
                I[int((num%10))]

        return roman

solution = Solution()
result = solution.intToRoman(1)
print(result)
print(type(result))