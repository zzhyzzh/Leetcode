class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        peri = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    peri += 4
                    if j != len(grid[0]) - 1 and grid[i][j + 1] == 1:
                        peri -= 2
                    if i != len(grid) - 1 and grid[i + 1][j] == 1:
                        peri -= 2
        return peri

solution = Solution()
result = solution.islandPerimeter(
    [[0,1,0,0],
     [1,1,1,0],
     [0,1,0,0],
     [1,1,0,0]])
print(result)
print(type(result))