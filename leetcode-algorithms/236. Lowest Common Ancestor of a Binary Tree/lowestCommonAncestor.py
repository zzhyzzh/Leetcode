# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """

        def search(root):
            if not root:
                return None
            elif root.val == p.val or root.val == q.val:
                exist_left, _ = search(root.left)
                exist_right, _ = search(root.right)
                if exist_left or exist_right:
                    return True, root
                else:
                    return True, None
            else:
                exist_left, left = search(root.left)
                exist_right, right = search(root.right)
                if exist_left and exist_right:
                    return True, root
                elif exist_left:
                    return True, left
                elif exist_right:
                    return True, right
                else:
                    return False, None

        _, ca = search(root)
        return ca



