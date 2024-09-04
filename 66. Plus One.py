'''

ou are given a large integer represented as an integer array digits, where each digits[i]
is the ith digit of the integer. The digits are ordered from most significant to least
significant in left-to-right order. The large integer does not contain any leading 0's.

Increment the large integer by one and return the resulting array of digits.

'''


from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1

        for i in range(len(digits) - 1, -1, -1):
            carry, digits[i] = divmod(digits[i] + carry, 10)

        return digits if not carry else [carry] + digits
