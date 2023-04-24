# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        def recurse_tree(current_node):
            # If reached the end of a branch, return None.
            if not current_node:
                return None

            # Left Recursion
            left = recurse_tree(current_node.left)

            # Right Recursion
            right = recurse_tree(current_node.right)

            # If the current node is one of p or q
            if current_node == p or current_node == q:
                return current_node

            # If both left and right are not None, it means we found both p and q in the subtree rooted at the current node.
            if left and right:
                return current_node

            # Return the non-None value if either left or right is not None, else return None.
            return left if left else right

        # Traverse the tree and return the result
        return recurse_tree(root)
