# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root == None:
            return root
        left = None
        right = None
        if root.left:
            left = self.invertTree(root.left)
        if root.right:
            right = self.invertTree(root.right)     
        root.right = left
        root.left = right
        return root