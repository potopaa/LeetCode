"""
Given an integer x, return true if x is a palindrome , and false otherwise.
"""


class Solution:
    def isPalindrome(self, x: int) -> bool:

        if x < 0:
            return False

        new = 0
        orig = x

        while x:
            x, d = divmod(x, 10)

            new = new * 10 + d
