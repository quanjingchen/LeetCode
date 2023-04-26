# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        path = []
        def helper(node):
            nonlocal path
            if not node:
                path.append('null')
            else:
                helper(node.left)
                helper(node.right)
                path.append(str(node.val))
        helper(root)
        return ",".join(path)
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        
        def helper(list):
                
            if list[-1] == 'null':
                list.pop()
                return None
            node = TreeNode(list[-1])
            list.pop()
            node.right = helper(list)
            node.left = helper(list)
            return node
        
        return helper(data.split(','))
           
        
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))