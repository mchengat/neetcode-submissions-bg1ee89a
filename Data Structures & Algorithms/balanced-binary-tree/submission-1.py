# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return self.depth(root) != -1

    def depth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        leftsubtree = self.depth(root.left)
        if leftsubtree == -1:
            return -1

        rightsubtree = self.depth(root.right)
        if rightsubtree == -1:
            return -1

        if abs(leftsubtree - rightsubtree) > 1:
            return -1

        return 1 + max(leftsubtree, rightsubtree)