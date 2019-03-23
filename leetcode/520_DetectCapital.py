# https://leetcode.com/problems/detect-capital/
# judge whether the usage of capitals in it is right or not.

class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if word.isupper():
            return True
        elif word.islower():
            return True
        elif len(word) > 1 and word[0].isupper() and word[1:].islower():
            return True
        else:
            return False

if __name__=="__main__":
    obj = Solution()
    param_1 = obj.detectCapitalUse("FAG")
    print(param_1)

# better solution
# def detectCapitalUse(self, word):
#     return word.isupper() or word.islower() or word.istitle()