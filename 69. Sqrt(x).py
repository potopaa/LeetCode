'''

Given a non-negative integer x, return the square root of x rounded down to the nearest integer.
The returned integer should be non-negative as well.

You must not use any built-in exponent function or operator.

For example, do not use pow(x, 0.5) in c++ or x ** 0.5 in python.

'''


class Solution:
    def mySqrt(self, x: int) -> int:

        if x < 2:
            return x

        l, r = 1, x // 2

        while l <= r:

            mid = (l + r) // 2

            sq = mid * mid

            if sq == x:
                return mid

            if sq > x:

                r = mid - 1

            else:
                l = mid + 1

        return r





