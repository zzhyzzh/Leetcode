class Solution(object):
    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        mask = [1] * len(A[0])
        for i in range(len(A)):
            A[i] = list(map(lambda a, b: a ^ b, A[i][::-1], mask))

        return A

solution = Solution()
result = solution.flipAndInvertImage([[1,1,0],[1,0,1],[0,0,0]])
print(result)
print(type(result))