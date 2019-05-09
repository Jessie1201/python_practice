# https://leetcode.com/problems/shortest-distance-to-a-character/
# shortest distance from the character C in the string.

# O(n)
class Solution:
    def shortestToChar(self, S: str, C: str):
        res = []
        for i in range(len(S)):
            dis = dis1 = dis2 = 0
            if C in S[i:] and C not in S[:i]:
                while S[i+dis] != C:
                    dis += 1
                res.append(dis)
            elif C not in S[i:] and C in S[:i]:
                while S[i-dis] != C:
                    dis += 1
                res.append(dis)
            else:
                while S[i+dis1] != C:
                    dis1 += 1
                while S[i-dis2] != C:
                    dis2 += 1
                res.append(min(dis1, dis2))
        return res


if __name__=="__main__":
    obj = Solution()
    param_1 = obj.shortestToChar("loveleetcode", "e")
    print(param_1)