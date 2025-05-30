from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if root is None:
            return None

        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else:
            if not root.left:
                return root.right
            if not root.right:
                return root.left

            min_node = self.find_min(root.right)
            root.val = min_node.val
            root.right = self.deleteNode(root.right, min_node.val)

        return root

    def find_min(self, node: TreeNode) -> TreeNode:
        while node.left:
            node = node.left
        return node
