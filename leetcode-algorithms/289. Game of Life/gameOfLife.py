class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        def getUp(board, i, j):
            if i == 0:
                return 0
            else:
                return board[i - 1][j]
        def getDown(board, i, j):
            if i == len(board) - 1:
                return 0
            else:
                return board[i + 1][j]
        def getLeft(board, i, j):
            if j == 0:
                return 0
            else:
                return board[i][j - 1]
        def getRight(board, i, j):
            if j == len(board[0]) - 1:
                return 0
            else:
                return board[i][j + 1]
        def getNW(board, i, j):
            if i == 0 or j == 0:
                return 0
            else:
                return board[i - 1][j - 1]
        def getNE(board, i, j):
            if i == 0 or j == len(board[0]) - 1:
                return 0
            else:
                return board[i - 1][j + 1]
        def getSW(board, i, j):
            if i == len(board) - 1 or j == 0:
                return 0
            else:
                return board[i + 1][j - 1]
        def getSE(board, i, j):
            if i == len(board) - 1 or j == len(board[0]) - 1:
                return 0
            else:
                return board[i + 1][j + 1]
        def isLive(state):
            if state == 0 or state == 2:
                return 0
            else:
                return 1
        def willLive(state):
            if state == 0 or state == 1:
                return 0
            else:
                return 1
        def getSum(board, i, j):
            up = isLive(getUp(board, i, j))
            down = isLive(getDown(board, i, j))
            left = isLive(getLeft(board, i, j))
            right = isLive(getRight(board, i, j))
            NW = isLive(getNW(board, i, j))
            NE = isLive(getNE(board, i, j))
            SW = isLive(getSW(board, i, j))
            SE = isLive(getSE(board, i, j))
            return up + down + left + right + NW + NE + SW + SE
        row = len(board)
        col = len(board[0])
        for i in range(row):
            for j in range(col):
                neighbor = getSum(board, i, j)
                if isLive(board[i][j]):
                    if neighbor < 2 or neighbor > 3:
                        board[i][j] = 1
                    else:
                        board[i][j] = 3
                else:
                    if neighbor == 3:
                        board[i][j] = 2
        for i in range(row):
            for j in range(col):
                board[i][j] = willLive(board[i][j])

solution = Solution()
result = solution.gameOfLife([[0,1,0],[0,0,1],[1,1,1],[0,0,0]])
print(result)
print(type(result))
