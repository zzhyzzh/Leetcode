class DSU(object):
    def __init__(self, grid):
        self.row = len(grid)
        self.col = len(grid[0])
        self.parent = list(range(self.row * self.col))
        self.rank = [0] * self.row * self.col
        self.count = 0
        self.bordered = set()

    def find(self, pos):
        if self.parent[pos] != pos:
            self.parent[pos] = self.find(self.parent[pos])
        return self.parent[pos]

    def union(self, x1, x2, y1, y2, border):
        x_parent, y_parent = self.find(x1 * self.col + x2), self.find(y1 * self.col + y2)
        if x_parent == y_parent:
            return False
        elif self.rank[x_parent] < self.rank[y_parent]:
            self.parent[x_parent] = y_parent
            if border:
                self.bordered.add(y_parent)
        elif self.rank[x_parent] > self.rank[y_parent]:
            self.parent[y_parent] = x_parent
            if border:
                self.bordered.add(x_parent)
        else:
            self.parent[y_parent] = x_parent
            if border:
                self.bordered.add(x_parent)
            self.rank[x_parent] += 1

        self.count -= 1
        return True


class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        if not any(board):
            return
        row = len(board)
        col = len(board[0])
        dsu = DSU(board)
        for i in range(row):
            for j in range(col):
                if board[i][j] == "O":
                    if j + 1 < col and board[i][j + 1] == "O":
                        border = i == 0 or i == row - 1 or j == 0 or j == col - 2
                        dsu.union(i, j, i, j + 1, border)
                    # look down
                    if i + 1 < row and board[i + 1][j] == "O":
                        border = i == 0 or i == row - 2 or j == 0 or j == col - 1
                        dsu.union(i, j, i + 1, j, border)
        for i in range(1, row - 1):
            for j in range(1, col - 1):
                if board[i][j] == "O":
                    parent = dsu.find(i * col + j)
                    if parent not in dsu.bordered:
                        board[i][j] = "X"