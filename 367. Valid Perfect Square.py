"""

Given a positive integer num, return true if num is a perfect square or false otherwise.

A perfect square is an integer that is the square of an integer. In other words,
it is the product of some integer with itself.

You must not use any built-in library function, such as sqrt.

"""



class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        
        if num == 1:
            return True


        l, r = 1, num // 2

        while l <= r:

            mid = (l + r) // 2

            squere = mid * mid

            if squere == num:
                return True

            if squere < num:
                l = mid + 1
            else:
                r = mid - 1

        return False
