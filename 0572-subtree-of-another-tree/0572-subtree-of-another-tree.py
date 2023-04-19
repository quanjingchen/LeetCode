class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if root is None:
            return False

        if self.isIdentical(root, subRoot):
            return True

        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

    def isIdentical(self, node1: Optional[TreeNode], node2: Optional[TreeNode]) -> bool:
        if node1 is None or node2 is None:
            return node1 is None and node2 is None

        return (node1.val == node2.val and
                self.isIdentical(node1.left, node2.left) and
                self.isIdentical(node1.right, node2.right))
