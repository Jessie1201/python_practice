# find the longest common prefix string amongst an array of strings.
# Input: ["flower","flow","flight"]
# Output: "fl"

class Solution:
    def longestCommonPrefix(self, strs) -> str:
        short = ''
        for el in strs:
            if all(len(el) <= len(oth) for oth in strs):
                short = el
        stack = ''
        for i, ch in enumerate(short):
            if all(ch == el[i] for el in strs):
                stack += ch
            else: break
        return stack



if __name__=="__main__":
    obj = Solution()
    param_1 = obj.longestCommonPrefix(["aca","cba"])
    print(param_1)
