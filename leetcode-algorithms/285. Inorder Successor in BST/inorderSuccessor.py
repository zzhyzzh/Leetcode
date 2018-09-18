# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderSuccessor(self, root, p):
        """
        :type root: TreeNode
        :type p: TreeNode
        :rtype: TreeNode
        """
        node = root
        preNode = None
        while node and node.val != p.val:
            if p.val < node.val:
                preNode = node
                node = node.left
            elif p.val > node.val:
                node = node.right
        if node.right:
            stack = []
            temp = node.right
            while stack or temp:
                while temp:
                    stack.append(temp)
                    temp = temp.left
                temp = stack.pop()
                return temp
        elif preNode:
            return preNode
        else:
            return None
