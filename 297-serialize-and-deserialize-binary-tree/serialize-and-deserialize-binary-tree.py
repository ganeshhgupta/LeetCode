from collections import deque

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string."""
        if not root:
            return ""  # <-- handle empty tree

        res = []
        q = deque([root])

        while q:
            node = q.popleft()
            if node:
                res.append(str(node.val))
                q.append(node.left)
                q.append(node.right)
            else:
                res.append("None")

        return ",".join(res)


    def deserialize(self, data):
        """Decodes your encoded data to tree."""
        if not data:
            return None  # <-- empty string case

        nodes = data.split(",")
        if nodes[0] == "None":  # <-- handle serialized None root
            return None

        root = TreeNode(int(nodes[0]))
        q = deque([root])
        i = 1

        while q and i < len(nodes):
            node = q.popleft()

            # Left child
            if nodes[i] != "None":
                node.left = TreeNode(int(nodes[i]))
                q.append(node.left)
            i += 1

            # Right child
            if i < len(nodes) and nodes[i] != "None":
                node.right = TreeNode(int(nodes[i]))
                q.append(node.right)
            i += 1

        return root
