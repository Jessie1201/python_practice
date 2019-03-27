# https://leetcode.com/problems/student-attendance-record-i/
# doesn't contain more than one 'A' (absent) or more than two continuous 'L' (late).

import collections
class Solution:
    def checkRecord(self, s: str) -> bool:
        count = collections.Counter(s)
        if count['A'] > 1:
            return False
        # with at least 3 L
        for i in range(len(s)-2):
            if s[i] == s[i+1] == s[i+2] == 'L':
                return False
        return True
        

if __name__=="__main__":
    obj = Solution()
    param_1 = obj.checkRecord("LALL")
    print(param_1)
