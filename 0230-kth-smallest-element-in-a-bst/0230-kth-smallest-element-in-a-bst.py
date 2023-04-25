# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        list = []
        def traverseInorder(node):
            if not node:
                return
            traverseInorder(node.left)
            list.append(node.val)
            traverseInorder(node.right)
            
        traverseInorder(root)
        return list[k - 1]
        