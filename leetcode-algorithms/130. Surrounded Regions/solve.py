class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        if board == []:
            return
        def search(i, j):
            if j not in range(len(board[0])) or i not in range(len(board)):
                return
            if board[i][j] == "O":
                board[i][j] = "S"
                if i == 0:
                    search(i + 1, j)
                elif i == len(board):
                    search(i - 1, j)
                elif j == 0:
                    search(i, j + 1)
                elif j == len(board[0]):
                    search(i, j - 1)
                else:
                    search(i, j + 1)
                    search(i, j - 1)
                    search(i + 1, j)
                    search(i - 1, j)
            else:
                return

        for m in range(0, len(board[0])):
            search(0, m)
            search(len(board) - 1, m)

        for m in range(1, len(board) - 1):
            search(m, 0)
            search(m, len(board[0]) - 1)

        for n in range(0, len(board[0])):
            for m in range(0, len(board)):
                if board[m][n] == "S":
                    board[m][n] = "O"
                elif board[m][n] == "O":
                    board[m][n] = "X"

solution = Solution()
result = solution.solve([["X","O","X","O","X","O"],
                         ["O","X","O","X","O","X"],
                         ["X","O","X","O","X","O"],
                         ["O","X","O","X","O","X"]])
print(result)
print(type(result))
