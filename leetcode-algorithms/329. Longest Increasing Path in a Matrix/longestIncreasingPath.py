class Solution(object):
    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        if not any(matrix):
            return 0
        row = len(matrix)
        col = len(matrix[0])
        dp = [0] * row * col
        maxLength = 0

        def DFS(i, j, maxLength):
            center = matrix[i][j]
            if i == 0:
                up = -float("inf")
            else:
                up = matrix[i - 1][j]
            if i == row - 1:
                down = -float("inf")
            else:
                down = matrix[i + 1][j]
            if j == 0:
                left = -float("inf")
            else:
                left = matrix[i][j - 1]
            if j == col - 1:
                right = -float("inf")
            else:
                right = matrix[i][j + 1]
            if center >= max(left, right, up, down):
                if dp[i * col + j] == 0:
                    dp[i * col + j] = 1
                maxLength = max(1, maxLength)
                return 1, maxLength
            else:
                leftWard = 1
                rightWard = 1
                upWard = 1
                downWard = 1
                if center < left:
                    if dp[i * col + j - 1] == 0:
                        dp[i * col + j - 1], _ = DFS(i, j - 1, maxLength)
                    leftWard = 1 + dp[i * col + j - 1]
                if center < right:
                    if dp[i * col + j + 1] == 0:
                        dp[i * col + j + 1], _ = DFS(i, j + 1, maxLength)
                    rightWard = 1 + dp[i * col + j + 1]
                if center < up:
                    if dp[(i - 1) * col + j] == 0:
                        dp[(i - 1) * col + j], _ = DFS(i - 1, j, maxLength)
                    upWard = 1 + dp[(i - 1) * col + j]
                if center < down:
                    if dp[(i + 1) * col + j] == 0:
                        dp[(i + 1) * col + j], _ = DFS(i + 1, j, maxLength)
                    downWard = 1 + dp[(i + 1) * col + j]
                dp[i * col + j] = max(leftWard, rightWard, upWard, downWard)
                maxLength = max(maxLength, dp[i * col + j])
                return dp[i * col + j], maxLength

        for i in range(row):
            for j in range(col):
                _, maxLength = DFS(i, j, maxLength)

        return maxLength

solution = Solution()
result = solution.longestIncreasingPath(
[[7,7,5],
 [2,4,6],
 [8,2,0]]
)
print(result)
print(type(result))