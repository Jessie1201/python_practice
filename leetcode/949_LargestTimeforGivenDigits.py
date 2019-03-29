# https://leetcode.com/problems/largest-time-for-given-digits/
# Given an array of 4 digits, return the largest 24 hour time that can be made.

import collections
import itertools
class Solution:
    def largestTimeFromDigits(self, A) -> str:
        A_org = A[:]
        count = collections.Counter(A)
        res = []
        if 2 in count and (0 in count or 1 in count or 3 in count or count[2] >= 2):
            res.append(2)
            A.remove(2)
            hr = max([num for num in A if num <= 3])
            res.append(hr)
            A.remove(hr)
            A = [str(el) for el in A]
            per = [int("".join(perm)) for perm in itertools.permutations(''.join(A)) if int("".join(perm))<=59]
            if per:
                mi = max(per)
                res.append(mi)
            else:
                A = A_org
                res = []
        if A == A_org and 1 in count:
            res.append(1)
            A.remove(1)
            res.append(max(A))
            A.remove(max(A))
            A = [str(el) for el in A]
            per = [int("".join(perm)) for perm in itertools.permutations(''.join(A)) if int("".join(perm))<=59]
            if per:
                mi = max(per)
                res.append(mi)
            else:
                return ''
        elif A == A_org and 0 in count:
            res.append(0)
            A.remove(0)
            res.append(max(A))
            A.remove(max(A))
            A = [str(el) for el in A]
            per = [int("".join(perm)) for perm in itertools.permutations(''.join(A)) if int("".join(perm))<=59]
            if per:
                mi = max(per)
                res.append(mi)
            else:
                return ''
        elif A == A_org:
            return ''
        if len(str(res[2])) == 1:
            res[2] = '0' + str(res[2])
        return str(res[0]) + str(res[1]) + ':' + str(res[2])
        


if __name__=="__main__":
    obj = Solution()
    param_1 = obj.largestTimeFromDigits([5,5,5,5])
    print(param_1)

# better solusion
def largestTimeFromDigits(self, A):
    return max(["%d%d:%d%d" % t for t in itertools.permutations(A) if t[:2] < (2, 4) and t[2] < 6] or [""])