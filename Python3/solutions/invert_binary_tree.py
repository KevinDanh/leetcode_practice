class Solution1:    
    def invertTree(self, root):
        if not root:
            return None

        stack = [root]

        while stack:
            current = stack.pop()
            current.left, current.right = current.right, current.left
            if current.left:
                stack.append(current.left)
            if current.right:
                stack.append(current.right)

        return root