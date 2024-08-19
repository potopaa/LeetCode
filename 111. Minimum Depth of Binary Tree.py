'''

Given a binary tree, find its minimum depth.
The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.
Note: A leaf is a node with no children.

'''
from collections import deque
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:

        if not root:
            return 0

        q = deque([(root, 1)])

        while q:
            cur, depth = q.popleft()

            if not cur.left and not cur.right:
                return depth

            if cur.left:
                q.append((cur.left, depth + 1))
            if cur.right:
                q.append((cur.right, depth + 1))
