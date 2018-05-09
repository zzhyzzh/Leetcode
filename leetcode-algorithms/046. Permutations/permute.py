class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        combi_list = []
        if nums == []:
            return []
        if len(nums) == 1:
            return [nums]
        else:
            permute_list = self.permute(nums[1:])
            for perm in permute_list:
                for i in range(len(perm) + 1):
                    perm_ = perm[0:i] + [nums[0]] + perm[i:]
                    combi_list.append(perm_)

        return combi_list

solution = Solution()
result = solution.permute([1,2,3])
print(result)
print(type(result))