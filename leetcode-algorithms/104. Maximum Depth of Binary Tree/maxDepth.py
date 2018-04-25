# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return 0
        if root.left == None and root.right == None:
            return 1
        depth_left, depth_right = 0, 0
        if root.left != None:
            depth_left = 1 + self.maxDepth(root.left)
        if root.right != None:
            depth_right = 1 + self.maxDepth(root.right)

        return max(depth_left, depth_right)


solution = Solution()
result = solution.maxDepth()
print(result)
print(type(result))