# https://leetcode.com/problems/most-common-word/
# Given a paragraph and a list of banned words, return the most frequent word that is not in the list of banned words.  It is guaranteed there is at least one word that isn't banned, and that the answer is unique.
# Input: 
# paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
# banned = ["hit"]
# Output: "ball"

import string
from statistics import mode

class Solution:
    def mostCommonWord(self, paragraph: str, banned) -> str:
        # replace punctuations with space
        for el in paragraph:
            if el in string.punctuation:
                # note to use the same variable name for recursive
                paragraph = paragraph.replace(el, ' ')
        li = paragraph.split()
        li_lower = []
        for el in li:
            li_lower.append(el.lower())
        # remove words from banned list
        li_final = []
        for el in li_lower:
            if el not in banned:
                li_final.append(el)
        return mode(li_final)


if __name__=="__main__":
    obj = Solution()
    # param_1 = obj.mostCommonWord("a a a a b,b,b,c c", ["a"])
    param_1 = obj.mostCommonWord("Bob hit a ball, the hit BALL flew far after it was hit.", ["hit"])
    print(param_1)