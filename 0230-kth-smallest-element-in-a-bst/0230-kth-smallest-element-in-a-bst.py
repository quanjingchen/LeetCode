# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        res = None
        counter = 0
        def traverseInorder(node):
            nonlocal res, counter
            if res or not node:
                return
            traverseInorder(node.left)
            counter += 1
            if counter == k:
                res = node.val
            traverseInorder(node.right)
            
        traverseInorder(root)
        return res

