"""

We are playing the Guess Game. The game is as follows:

I pick a number from 1 to n. You have to guess which number I picked.

Every time you guess wrong, I will tell you whether the number I picked is higher or lower than your guess.

You call a pre-defined API int guess(int num), which returns three possible results:

-1: Your guess is higher than the number I picked (i.e. num > pick).
1: Your guess is lower than the number I picked (i.e. num < pick).
0: your guess is equal to the number I picked (i.e. num == pick).
Return the number that I picked.

"""


# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0

def guess(num: int) -> int:

    class Solution:
        def guessNumber(self, n: int) -> int:
            l, r = 1, n

            while l <= r:

                mid = (l + r) // 2

                check = guess(mid)

                if check == 0:
                    return mid

                if check < 0:
                    r = mid - 1

                else:
                    l = mid + 1
