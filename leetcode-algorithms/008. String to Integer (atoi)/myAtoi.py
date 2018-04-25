import re

INT_MAX = 2147483647
INT_MIN = -2147483648

class Solution:
    def str_to_int(self, intStr):
        switcher = {
            "0": 0,
            "1": 1,
            "2": 2,
            "3": 3,
            "4": 4,
            "5": 5,
            "6": 6,
            "7": 7,
            "8": 8,
            "9": 9,
        }
        return switcher.get(intStr)

    def myAtoi(self, intStr):
        """
        :type intStr: str
        :rtype: int
        """
        intVal = 0
        isNegative = 1
        intStr = intStr.lstrip(" ")
        if re.match('-', intStr):
            isNegative = -1
            intStr = intStr[1:]
        elif re.match('\+', intStr):
            isNegative = 1
            intStr = intStr[1:]
        p = re.match(r'[0-9]*', intStr).span()
        intStr = intStr[p[0]:p[1]]
        for i in range(0, len(intStr)):
            intVal = self.str_to_int(intStr[i]) + intVal * 10
        if isNegative * intVal > INT_MAX:
            return INT_MAX
        elif isNegative * intVal < INT_MIN:
            return INT_MIN
        else:
            return intVal * isNegative

solution = Solution()
result = solution.myAtoi("123")
print(result)
