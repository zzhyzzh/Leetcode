# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if len(preorder) == 0:
            return None
        elif len(preorder) == 1:
            return TreeNode(preorder[0])
        elif len(preorder) == 2:
            root = TreeNode(preorder[0])
            if inorder[0] == preorder[1]:
                root.left = TreeNode(preorder[1])
            else:
                root.right = TreeNode(preorder[1])
            return root
        else:
            root = TreeNode(preorder[0])
            rootPos = inorder.index(preorder[0])
            leftSubLen = rootPos
            rightSubLen = len(inorder) - leftSubLen - 1
            root.left = self.buildTree(preorder[1:1 + leftSubLen], inorder[:leftSubLen])
            root.right = self.buildTree(preorder[1 + leftSubLen:], inorder[leftSubLen + 1:])

            return root

