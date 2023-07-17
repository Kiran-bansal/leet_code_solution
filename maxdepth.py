class Solution(object):
    def maxDepth(self, root):
        if not root:
            return 0
        queue = [root]
        depth = 0
        while queue:
            depth += 1
            for _ in range(len(queue)):
                node = queue.pop(0)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return depth
