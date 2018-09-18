# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if len(nums) == 0:
            return None
        elif len(nums) == 1:
            return TreeNode(nums[0])
        elif len(nums) == 2:
            root = TreeNode(nums[1])
            root.left = TreeNode(nums[0])
        elif len(nums) >= 3:
            middle = len(nums)//2
            root = TreeNode(nums[middle])
            root.left = self.sortedArrayToBST(nums[0:middle])
            root.right = self.sortedArrayToBST(nums[middle + 1:])
        return root