'''

You are given a string s consisting of lowercase English letters.
A duplicate removal consists of choosing two adjacent and equal letters and removing them.

We repeatedly make duplicate removals on s until we no longer can.

Return the final string after all such duplicate removals have been made.
It can be proven that the answer is unique.

'''


class Solution:
    def reverseWords(self, s: str) -> str:
        
        words = s.split(' ')

        for i in range(len(words)):

            words[i] = words[i][::-1]

        return ' '.join(words)
