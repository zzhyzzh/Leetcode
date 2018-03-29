class Solution:
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        num = 0
        for str in S:
            if str in J:
                num += 1

        return num

solution = Solution()
result = solution.numJewelsInStones("aA", "aAAbbbb")
print(result)
print(type(result))