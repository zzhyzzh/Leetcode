class DSU(object):
    def __init__(self, grid):
        self.row = len(grid)
        self.col = len(grid[0])
        self.parent = []
        self.rank = []
        self.count = 0
        self.unionCount = 0

        for i in range(self.row):
            for j in range(self.col):
                self.rank.append(0)
                if grid[i][j] == "1":
                    self.parent.append(i * self.col + j)
                    self.count += 1
                elif grid[i][j] == "0":
                    self.parent.append(-1)
        self.unionCount = self.count

    def find(self, pos):
        if self.parent[pos] != pos:
            self.parent[pos] = self.find(self.parent[pos])
        return self.parent[pos]

    def union(self, x1, x2, y1, y2):
        x_parent, y_parent = self.find(x1 * self.col + x2), self.find(y1 * self.col + y2)
        if x_parent == y_parent:
            return False
        elif self.rank[x_parent] < self.rank[y_parent]:
            self.parent[x_parent] = y_parent
        elif self.rank[x_parent] > self.rank[y_parent]:
            self.parent[y_parent] = x_parent
        else:
            self.parent[y_parent] = x_parent
            self.rank[x_parent] += 1

        self.unionCount -= 1
        return True


class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        row = len(grid)
        col = len(grid[0])
        dsu = DSU(grid)
        for i in range(row):
            for j in range(col):
                if grid[i][j] == "1":
                    # look right
                    if j + 1 < col and grid[i][j + 1] == "1":
                        dsu.union(i, j, i, j + 1)
                    # look down
                    if i + 1 < row and grid[i + 1][j] == "1":
                        dsu.union(i, j, i + 1, j)

        return dsu.unionCount


solution = Solution()
result = solution.numIslands(
[["1","1","1","1","0"],
 ["1","1","0","1","0"],
 ["1","1","0","0","0"],
 ["0","0","0","0","0"]]
)
print(result)
print(type(result))