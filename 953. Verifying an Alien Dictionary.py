"""

n an alien language, surprisingly, they also use English lowercase letters,
but possibly in a different order. The order of the alphabet is some permutation of lowercase letters.

Given a sequence of words written in the alien language, and the order of the alphabet,
return true if and only if the given words are sorted lexicographically in this alien language.

"""

from typing import List


class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:

        ord_d = {l:i for i, l in enumerate(order)}

        for w1, w2 in zip(words, words[1:]):
            for i, j in zip(w1, w2):
                if i != j:
                    if ord_d[i] > ord_d[j]:
                        return False
                    break
            if w1.startswith(w2) and w1 != w2:
                return False

        return True
    