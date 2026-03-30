# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.preIdx = 0
        self.inorderIndexMap = {}
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        self.inorderIndexMap = {val: idx for idx, val in enumerate(inorder)}
        return self._constructTree(preorder, 0, len(inorder) - 1)
    
    def _constructTree(self, preorder, inStart, inEnd):
        if inStart > inEnd:
            return None

        rootVal = preorder[self.preIdx]
        self.preIdx += 1
        root = TreeNode(rootVal)

        if inStart == inEnd:
            return root

        in_index = self.inorderIndexMap[rootVal]
        root.left = self._constructTree(preorder, inStart, in_index - 1)
        root.right = self._constructTree(preorder, in_index + 1, inEnd)
        return root