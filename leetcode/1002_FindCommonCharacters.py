# https://leetcode.com/problems/find-common-characters/
# all characters that show up in all strings within the list (including duplicates).

class Solution:
    def commonChars(self, A):
        res = []
        tem = A[1:]
        for ch in A[0]:
            if all(ch in el for el in tem):
                res.append(ch)
                for i in range(len(tem)):
                    tem[i] = tem[i][:tem[i].index(ch)] + tem[i][tem[i].index(ch)+1:]
        return res

if __name__=="__main__":
    obj = Solution()
    param_1 = obj.commonChars(["bella","label","roller"])
    print(param_1)

# better solution
class Solution:
    def commonChars(self, A):
        res = collections.Counter(A[0])
        for a in A:
            res &= collections.Counter(a)
        return list(res.elements())