# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        queue = [root]
        isLeft = True
        levelLength = len(queue)
        traversal = []
        while levelLength:
            level = []
            end = len(queue)
            for i in range(len(queue) - levelLength, end):
                level.append(queue[i].val)
                if queue[i].left:
                    queue.append(queue[i].left)
                if queue[i].right:
                    queue.append(queue[i].right)
            if isLeft:
                traversal.append(level)
                isLeft = False
            elif not isLeft:
                traversal.append(level[::-1])
                isLeft = True
            levelLength = len(queue) - end

        return traversal

