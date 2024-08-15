'''

Given an array nums of integers, return how many of them contain an even number of digits.

'''

from typing import List


class Solution:
    def findNumbers(self, nums: List[int]) -> int:

        def d_num(num):

            ret = 0

            while num:
                num //= 10
                ret += 1

            return ret

        ans = 0

        for num in nums:
            ans += 0 if d_num(num) % 2 else 1

        return ans 