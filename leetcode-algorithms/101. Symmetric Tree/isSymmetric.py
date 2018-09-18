# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        head = 0
        queue = [root]
        while True:
            temp = head
            i, j = temp, len(queue) - 1
            while i < j:
                if not queue[i]:
                    if queue[j]:
                        return False
                    elif not queue[j]:
                        i += 1
                        j -= 1
                elif not queue[j] or queue[i].val != queue[j].val:
                    return False
                else:
                    i += 1
                    j -= 1
            noneCount = 0
            for i in range(temp, len(queue)):
                head += 1
                if not queue[i]:
                    noneCount += 1
                    continue
                else:
                    queue.append(queue[i].left)
                    queue.append(queue[i].right)
            if noneCount == len(queue) - temp:
                return True
