'''

Given the root of a binary tree, return the postorder traversal of its nodes' values.

'''


from typing import Optional
from typing import List


class TreeNode:
    pass


class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []

        def helper(node):
            if node:
                helper(node.left)
                helper(node.right)
                ans.append(node.val)

        helper(root)

        return ans
