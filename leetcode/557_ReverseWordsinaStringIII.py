# https://leetcode.com/problems/reverse-words-in-a-string-iii/submissions/
# Given a string, you need to reverse the order of characters in each word within a sentence 
# while still preserving whitespace and initial word order.

class Solution:
    def reverseWords(self, s: str) -> str:
        org = s.split()
        reverse = []
        for el in org:
            reverse.append(el[::-1])
        return " ".join(reverse)

if __name__=="__main__":
    obj = Solution()
    param_1 = obj.reverseWords("Let's take LeetCode contest")
    print(param_1)