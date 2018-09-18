# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        stack = [root]
        traversal = []
        while stack:
            node = stack.pop()
            if node:
                traversal.append(node.val)
                stack.append(node.right)
                stack.append(node.left)

        return traversal


