"""

Given an n x n binary matrix image, flip the image horizontally, then invert it,
and return the resulting image.

To flip an image horizontally means that each row of the image is reversed.

For example, flipping [1,1,0] horizontally results in [0,1,1].
To invert an image means that each 0 is replaced by 1, and each 1 is replaced by 0.

For example, inverting [0,1,1] results in [1,0,0].

"""
from typing import List


class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:

        for row in image:

            l, r = 0, len(row) - 1

            while l <= r:

                row[l], row[r] = row[r], row[l]

                row[l] = 0 if row[l] else 1

                if l != r:
                    row[r] = 0 if row[r] else 1

                l += 1
                r -= 1

        return image
    