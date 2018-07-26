class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        digits = digits[::-1]
        digits[0] += 1
        for i in range(len(digits)):
            if digits[i] == 10:
                digits[i] = 0
                if i == len(digits) - 1:
                    digits.append(1)
                    return digits[::-1]
                else:
                    digits[i + 1] += 1

        return digits[::-1]


solution = Solution()
result = solution.plusOne([1,2,3])
print(result)
print(type(result))