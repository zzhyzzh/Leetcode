# -*- coding: utf-8 -*-
"""
Created on Wed Feb 28 21:26:36 2018

@author: zzhno
"""

class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)):
            remain = target - nums[i]
            if remain in nums:
                j = nums.index(remain)
                if j != i:
                    break
        
        return [i, j]

def main():
    solution = Solution()
    result = solution.twoSum([2, 7, 11, 15], 9)
    print(result)

if __name__ == '__main__':
    main()