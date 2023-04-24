# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        list = []
        def dfs(node):
            if not node:
                return
            dfs(node.left)
            list.append(node.val)
            dfs(node.right)
        dfs(root)
        for i in range(len(list) - 1):
            if list[i] >= list[i + 1]:
                return False
        return True
        