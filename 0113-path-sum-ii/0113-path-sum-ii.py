# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        paths = []
        path = []
        if root == None:
            return paths
        def traverse(node, sum):
            nonlocal paths, path
            
            if not node:
                return

            path.append(node.val)
            sum -= node.val
            if node.left == None and node.right == None:
                if sum == 0:
                    paths.append(path[:])
                
            traverse(node.left, sum)
            traverse(node.right, sum)
            path.pop()      
                
        traverse(root, targetSum)
        return paths