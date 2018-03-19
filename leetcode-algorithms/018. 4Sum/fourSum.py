class Solution:
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        solution_set = []
        nums.sort()
        if len(nums) < 4:
            return solution_set
        for L in range(0, len(nums) - 3):
            if L > 0 and nums[L] == nums[L - 1]:
                L += 1
                continue
            M1 = L + 1
            while M1 < len(nums) - 2:
                if M1 > L + 1 and nums[M1] == nums[M1 - 1]:
                    M1 += 1
                    continue
                R = len(nums) - 1
                M2 = M1 + 1
                while M2 < R:
                    sum = nums[L] + nums[M1] + nums[M2] + nums[R]
                    if sum > target:
                        R -= 1
                    elif sum < target:
                        M2 += 1
                    else:
                        solution_set += [[nums[L], nums[M1], nums[M2], nums[R]]]
                        while M2 < R and nums[M2 + 1] == nums[M2]:
                            M2 += 1
                        while M2 < R and nums[R - 1] == nums[R]:
                            R -= 1
                        R -= 1
                        M2 += 1
                M1 += 1

        return solution_set

solution = Solution()
result = solution.fourSum([1,-2,-5,-4,-3,3,3,5], -11)
print(result)
print(type(result))
