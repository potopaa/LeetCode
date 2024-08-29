'''

Given an integer n, return an array ans of length n + 1 such that for each i (0 <= i <= n), ans[i]
is the number of 1's in the binary representation of i.

'''

from typing import List

class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = [0]
        for i in range(1, n + 1):

            cur = 0

            while i:
                cur += i & 1
                i >>= 1

            ans.append(cur)

        return ans
