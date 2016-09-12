# no Liana solution


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        res = []

        def append_node(node):
            if node:
                res.append(str(node.val))
                append_node(node.left)
                append_node(node.right)
            else:
                res.append('n')

        append_node(root)
        return ' '.join(res)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        res = iter(data.split())

        def create_node():
            val = next(res)
            if val == 'n':
                return None
            node = TreeNode(int(val))
            node.left = create_node()
            node.right = create_node()
            return node

        return create_node()


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
