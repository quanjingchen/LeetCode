# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        ans = []
        if not root:
            return ans
        my_deque = deque()
        my_deque.append(root)
        while my_deque:
            level = []
            size = len(my_deque)
            for i in range(size):
                node = my_deque.popleft()
                level.append(node.val)
                if node.left:
                    my_deque.append(node.left)
                if node.right:
                    my_deque.append(node.right)
            ans.append(level[:])
            
        return ans
        