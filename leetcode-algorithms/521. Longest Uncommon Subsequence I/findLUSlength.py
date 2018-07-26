class Solution(object):
    def findLUSlength(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: int
        """
        return -1 if a == b else max(len(a), len(b))

solution = Solution()
result = solution.findLUSlength([4,1,2], [1,3,4,2])
print(result)
print(type(result))