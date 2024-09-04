'''

You are given an integer array nums consisting of n elements, and an integer k.

Find a contiguous subarray whose length is equal to k that has the maximum average
value and return this value.
Any answer with a calculation error less than 10^-5 will be accepted.

'''


from collections import deque
from typing import List


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:

        q = deque([])

        ans = -float('inf')

        cnt = 0
        cur = 0

        for i in range(len(nums)):
            cur += nums[i]
            cnt += 1

            if cnt == k:
                ans = max(ans, cur / k)

            if cnt > k:
                cur -= nums[i - k]
                ans = max(ans, cur / k)
        return ans
