# Definition for binary tree with next pointer.
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        if not root:
            return
        queue = [root]
        levelLength = len(queue)
        traversal = []
        while levelLength:
            level = []
            end = len(queue)
            for i in range(len(queue) - levelLength, end):
                level.append(queue[i])
                if queue[i].left:
                    queue.append(queue[i].left)
                if queue[i].right:
                    queue.append(queue[i].right)
            traversal.append(level)
            levelLength = len(queue) - end
        for level in traversal:
            for i, node in enumerate(level):
                if i < len(level) - 1:
                    node.next = level[i + 1]
