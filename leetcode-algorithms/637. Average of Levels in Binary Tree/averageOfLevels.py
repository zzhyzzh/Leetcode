# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        AoLs = []
        NoLs = []

        def treeSearch(level, root):
            if not root:
                return
            if len(AoLs) < level + 1:
                AoLs.append(root.val)
                NoLs.append(1)
            else:
                AoLs[level] += root.val
                NoLs[level] += 1
            treeSearch(level + 1, root.left)
            treeSearch(level + 1, root.right)

        treeSearch(0, root)
        for i in range(len(AoLs)):
            AoLs[i] /= float(NoLs[i])

        return AoLs