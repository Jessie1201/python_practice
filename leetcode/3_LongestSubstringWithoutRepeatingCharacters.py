# https://leetcode.com/problems/longest-substring-without-repeating-characters/
# length of the longest substring without repeating characters

# hash table
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dic = {}
        max_len = 0
        for i, ch in enumerate(s):
            if ch not in dic:
                dic[ch] = i
                max_len = max(max_len, len(dic))
            else:
                remove = []
                for key in dic:
                    if dic[key] <= dic[ch]:
                        remove.append(key)
                for key in remove:
                    del dic[key]
                dic[ch] = i
        return max_len


if __name__=="__main__":
    obj = Solution()
    param_1 = obj.lengthOfLongestSubstring("pwwkew")
    print(param_1)
