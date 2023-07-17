class Solution(object):
    def inorderTraversal(self, root):
        if not root:
            return []
        else:
            return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right)
