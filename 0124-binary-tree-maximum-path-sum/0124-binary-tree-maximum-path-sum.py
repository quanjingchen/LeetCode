# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:

        maxSum = -math.inf
        def traverse(node):
            nonlocal maxSum
            if not node:
                return 0
            
            #gain from the left
            gain_from_left = max(traverse(node.left), 0)
            #gain from the right
            gain_from_right = max(traverse(node.right), 0)
            maxSum = max(maxSum, gain_from_left + gain_from_right + node.val)
            return max(gain_from_left + node.val, gain_from_right + node.val)
        traverse(root)
        return maxSum
        
        
        