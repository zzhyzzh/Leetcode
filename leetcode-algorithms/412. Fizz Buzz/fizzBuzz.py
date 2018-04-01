class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        fb_list = []
        for i in range(1, n + 1):
            if i % 15 == 0:
                fb_list.append("FizzBuzz")
            elif i % 5 == 0:
                fb_list.append("Buzz")
            elif i % 3 == 0:
                fb_list.append("Fizz")
            else:
                fb_list.append(str(i))

        return fb_list

solution = Solution()
result = solution.fizzBuzz(15)
print(result)
print(type(result))