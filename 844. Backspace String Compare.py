'''

Given two strings s and t, return true if they are equal when both are typed into empty text editors.
 '#' means a backspace character.

Note that after backspacing an empty text, the text will continue empty.

'''


class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:

        def typing(s):

            stack = []

            for c in s:
                if c == "#":
                    if stack:
                        stack.pop()
                else:
                    stack.append(c)

            return ''.join(stack)

        return typing(s) == typing(t)


