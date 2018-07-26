class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        if len(a) <= len(b):
            a, b = b, a
        a, b = a[::-1], b[::-1]
        sumAB = ""
        sumUp = "0"
        for i in range(len(b)):
            if a[i] == "1" and b[i] == "1":
                sumAB += sumUp
                sumUp = "1"
            elif a[i] == "0" and b[i] == "0":
                sumAB += sumUp
                sumUp = "0"
            else:
                if sumUp == "1":
                    sumAB += "0"
                    sumUp = "1"
                else:
                    sumAB += "1"
                    sumUp = "0"
        for i in range(len(b), len(a)):
            if sumUp == "1":
                if a[i] == "1":
                    sumAB += "0"
                else:
                    sumAB += "1"
                    sumAB += a[i + 1:]
                    return sumAB[::-1]
            else:
                sumAB += a[i:]
                return sumAB[::-1]
        if sumUp == "1":
            sumAB += "1"

        return sumAB[::-1]

solution = Solution()
result = solution.addBinary("100","110010")
print(result)
print(type(result))