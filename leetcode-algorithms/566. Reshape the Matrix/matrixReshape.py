class Solution(object):
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        if len(nums) * len(nums[0]) != r * c:
            return nums
        mat = [[1] * c for i in range(r)]
        m = 0
        for i in range(len(nums)):
            for j in range(len(nums[0])):
                mat[int(m / c)][m % c] = nums[i][j]
                m += 1
        return mat

solution = Solution()
result = solution.matrixReshape([[1,2,3,4],
                                 [5,6,7,8]], 4, 2)
print(result)
print(type(result))