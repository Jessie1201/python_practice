# https://leetcode.com/problems/first-bad-version/
# Binary search for First Bad Version

# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        st = 1
        ed = n
        while st != ed:
            if isBadVersion(st+int((ed-st)/2)):
                ed = st+int((ed-st)/2)
            else:
                st = st+int((ed-st)/2) + 1
        return st
