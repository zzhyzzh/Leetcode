class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        ans = []

        def backtrack(s, left, right):
            if len(s) == 2 * n:
                ans.append(s)
                return

            if left < n:
                backtrack(s + "(", left + 1, right)
            if right < left:
                backtrack(s + ")", left, right + 1)

        backtrack('', 0, 0)
        return ans

solution = Solution()
result = solution.generateParenthesis(3)
print(result)
print(type(result))