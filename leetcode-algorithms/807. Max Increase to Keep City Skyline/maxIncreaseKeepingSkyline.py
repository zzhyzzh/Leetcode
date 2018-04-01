class Solution:
    def maxIncreaseKeepingSkyline(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        sum = 0
        skyline_horizontal = [max(row) for row in grid]
        skyline_vertical = [max([x[i] for x in grid]) for i in range(len(grid[0]))]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                sum += min(skyline_horizontal[i], skyline_vertical[j]) - grid[i][j]

        return sum

solution = Solution()
result = solution.maxIncreaseKeepingSkyline( [[3,0,8,4],[2,4,5,7],[9,2,6,3],[0,3,1,0]])
print(result)
print(type(result))
