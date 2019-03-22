# https://leetcode.com/problems/long-pressed-name/
# Input: name = "saeed", typed = "ssaaedd"
# Output: false

class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        if len(name) > len(typed):
            return False
        
        name_cp = name[0]
        typed_cp = typed[0]
        for i in range(1, len(name)):
            if name[i] != name[i-1]:
                name_cp += name[i]
        for i in range(1, len(typed)):
            if typed[i] != typed[i-1]:
                typed_cp += typed[i]
        if name_cp != typed_cp:
            return False
        
        i = j = 0
        while i < len(name)-1:
            if name[i] == name[i+1] == typed[j] == typed[j+1]:
                i += 1
                j += 1
            elif name[i] == typed[j] and typed[j] != typed[j+1]:
                i += 1
                j += 1
            elif name[i] == typed[j] == typed[j+1]:
                j += 1
            else:
                return False
        
        if len(typed[j:]) != typed[j:].count(typed[j]):
            return False
        return True



if __name__=="__main__":
    obj = Solution()
    param_1 = obj.isLongPressedName("kkiikcxmvzi","kkiikcxxmmvvzz")
    print(param_1)
