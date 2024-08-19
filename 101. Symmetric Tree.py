'''

Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).



Example 1:


Input: root = [1,2,2,3,4,4,3]
Output: true
Example 2:


Input: root = [1,2,2,null,3,null,3]
Output: false


Constraints:

The number of nodes in the tree is in the range [1, 1000].
-100 <= Node.val <= 100


Follow up: Could you solve it both recursively and iteratively?

'''

from typing import Optional

# Definition for a binary tree node.
 class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right



class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:

        q = deque([root])

        while q:

            level = []
            for _ in range(len(q)):

                cur = q.popleft()

                level.append(cur.val if cur else None)

                if cur:
                    q.append(cur.left)
                    q.append(cur.right)

            if len(level) > 1:
                n = len(level)
                fh, sh = level[:n // 2], level[n // 2:][::-1]
                if fh != sh:
                    return False

        return True




