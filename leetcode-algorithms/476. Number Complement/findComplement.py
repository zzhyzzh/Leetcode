class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        mask = 0
        temp = num
        while temp != 0:
            mask = mask << 1
            mask += 1
            temp = temp >> 1
        return num ^ mask

solution = Solution()
result = solution.findComplement(5)
print(result)
print(type(result))
