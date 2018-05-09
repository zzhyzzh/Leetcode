class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        vSum = 0
        hSum = 0

        for d in moves:
            if d == "U":
                vSum += 1
            elif d == "D":
                vSum -= 1
            elif d == "L":
                hSum -= 1
            elif d == "R":
                hSum += 1

        return (vSum + hSum) == 0

solution = Solution()
result = solution.judgeCircle("UD")
print(result)
print(type(result))