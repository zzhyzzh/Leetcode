class Solution(object):

    def isMatch(self, text, pattern):
        log = {}

        def dp(i, j):
            if (i, j) not in log:
                if j == len(pattern):
                    status = i == len(text)
                else:
                    first_match = i < len(text) and pattern[j] in {text[i], '.'}
                    if j + 1 < len(pattern) and pattern[j + 1] == '*':
                        status = dp(i, j + 2) or first_match and dp(i + 1, j)
                    else:
                        status = first_match and dp(i + 1, j + 1)

                log[i, j] = status
            return log[i, j]

        return dp(0, 0)


solution = Solution()
result = solution.isMatch("aab", "c*a*b")
print(result)
print(type(result))
