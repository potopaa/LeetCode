'''

Given an integer numRows, return the first numRows of Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:

Example 1:

Input: numRows = 5
Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
Example 2:

Input: numRows = 1
Output: [[1]]


Constraints:

1 <= numRows <= 30

'''

from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:

        dp = [[1], [1, 1]]

        if numRows < 3:
            return dp[:numRows]

        for _ in range(numRows - 2):

            next_row = [1]

            for i in range(1, len(dp[-1])):
                next_row.append(dp[-1][i] + dp[-1][i - 1])

            next_row += [1]
            dp.append(next_row)

        return dp

