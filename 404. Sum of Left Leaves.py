# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        
        ans = 0

        stack = [(root, None)]

        while stack:

            cur, is_left = stack.pop()

            if not cur.left and not cur.right and is_left:
                ans += cur.val

            if cur.left:
                stack.append((cur.left, 1))

            if cur.right:
                stack.append((cur.right, 0))

        return ans 
