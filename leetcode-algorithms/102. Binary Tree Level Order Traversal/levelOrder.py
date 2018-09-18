# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        queue = [root]
        traversal = []
        head = 0
        while len(queue[head:]):
            temp = queue[:]
            queue = []
            level = []
            while len(temp[head:]):
                if temp[head]:
                    level.append(temp[head].val)
                    queue.append(temp[head].left)
                    queue.append(temp[head].right)
                head += 1
            head = 0
            if level:
                traversal.append(level)

        return traversal
