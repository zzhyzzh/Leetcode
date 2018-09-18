# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    tilt = 0

    def calcSum(self, root):
        if root == None:
            return 0
        else:
            left = self.calcSum(root.left)
            right = self.calcSum(root.right)
            self.tilt += abs(left - right)
            return root.val + left + right

    def findTilt(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.calcSum(root)
        return self.tilt


