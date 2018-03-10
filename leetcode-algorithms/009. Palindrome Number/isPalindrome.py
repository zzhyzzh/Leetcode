class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        isPalindrome = True
        x = str(x)
        if len(x) == 1:
            return isPalindrome
        pos = 0
        while pos <= len(x)/2:
            if x[pos] != x[-(pos+1)]:
                isPalindrome = False
                break
            pos += 1
        return isPalindrome

solution = Solution()
result = solution.isPalindrome()
print(result)
print(type(result))