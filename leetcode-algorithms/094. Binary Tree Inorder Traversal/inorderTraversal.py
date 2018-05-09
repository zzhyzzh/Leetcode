# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        seq = []
        stack = []
        t = root
        while stack != [] or t:
            while t:
                stack.append(t)
                t = t.left
            t = stack.pop()
            seq.append(t.val)
            t = t.right

        return seq


def setTree(T, left, right):
    T.left = left
    T.right = right

    return T
t = setTree(TreeNode(1), None, setTree(TreeNode(2), TreeNode(3), None))
solution = Solution()
result = solution.inorderTraversal(t)
print(result)