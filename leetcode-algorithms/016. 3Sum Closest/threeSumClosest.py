class Solution:
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        L = 0
        distance = float('inf')
        while L < len(nums) - 2:
            if L > 0 and nums[L] == nums[L - 1]:
                L += 1
                continue
            R = len(nums) - 1
            M = L + 1
            while M < R:
                temp = nums[L] + nums[M] + nums[R] - target
                if abs(temp) < abs(distance):
                    distance = temp
                    if distance == 0:
                        return target
                if temp < 0:
                    M += 1
                elif temp > 0:
                    R -= 1
            L += 1

        return distance + target

solution = Solution()
result = solution.threeSumClosest([1,2,4,8,16,32,64,128], 82)
print(result)
print(type(result))
