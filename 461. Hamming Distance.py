'''

The Hamming distance between two integers is the number of positions at which the corresponding bits are different.
Given two integers x and y, return the Hamming distance between them.

'''


class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        ans = 0

        while x or y:
            ans += (x & 1) != (y & 1)
            x >>= 1
            y >>= 1

        return ans