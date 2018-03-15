class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        solution_set = []
        nums.sort()
        if len(nums) < 3 or nums[0] > 0 or nums[len(nums) - 1] < 0:
            return solution_set
        L = 0
        while L < len(nums) - 2 and nums[L] <= 0:
            if L > 0 and nums[L] == nums[L - 1]:
                L += 1
                continue
            R = len(nums) - 1
            M = L + 1
            while M < R:
                sum = nums[L] + nums[M] + nums[R]
                if sum > 0:
                    R -= 1
                elif sum < 0:
                    M += 1
                else:
                    solution_set += [[nums[L], nums[M], nums[R]]]
                    while M < R and nums[M + 1] == nums[M]:
                        M += 1
                    while M < R and nums[R - 1] == nums[R]:
                        R -= 1
                    R -= 1
                    M += 1
            L += 1

        return solution_set

solution = Solution()
result = solution.threeSum([-1,0,1,2,-1,-4])
print(result)
print(type(result))
