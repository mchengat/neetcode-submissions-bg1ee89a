# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.counter = 0
        self.smallest = 0

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def inorder(root: TreeNode | None):
            if root is None or self.counter >= k:
                return self.smallest
            inorder(root.left)
            self.counter += 1
            if self.counter == k:
                self.smallest = root.val

            inorder(root.right)
            return self.smallest

        return inorder(root)
        