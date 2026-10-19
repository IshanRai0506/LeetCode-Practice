class Solution:
    def increasingBST(self, root: TreeNode | None) -> TreeNode | None:
        dummy = TreeNode(0)
        curr = dummy

        def inorder(node):
            nonlocal curr

            if not node:
                return

            inorder(node.left)

            node.left = None
            curr.right = node
            curr = node

            inorder(node.right)

        inorder(root)
        return dummy.right