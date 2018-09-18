class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        setLists = [[], [], []]
        for i in range(9):
            setLists[0].append(set())
            setLists[1].append(set())
            setLists[2].append(set())
        for row in range(9):
            for col in range(9):
                num = board[row][col]
                if num == ".":
                    continue
                else:
                    num = int(num)
                if num not in setLists[0][row]:
                    setLists[0][row].add(num)
                else:
                    return False
                if num not in setLists[1][col]:
                    setLists[1][col].add(num)
                else:
                    return False
                gridNum = int(col / 3) + 3 * int(row / 3)
                if num not in setLists[2][gridNum]:
                    setLists[2][gridNum].add(num)
                else:
                    return False
        return True


solution = Solution()
result = solution.isValidSudoku([
  ["5","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
])
print(result)
print(type(result))