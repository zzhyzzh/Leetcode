class Solution(object):
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        self_list = []
        for i in range(left, right + 1):
            i_str = str(i)
            if "0" in i_str:
                continue
            for digit in i_str:
                if i % int(digit) != 0:
                    break
            else:
                self_list.append(i)

        return self_list

solution = Solution()
result = solution.selfDividingNumbers(1, 22)
print(result)
print(type(result))