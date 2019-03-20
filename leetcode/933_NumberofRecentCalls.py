# https://leetcode.com/problems/number-of-recent-calls/
# Write a class RecentCounter to count recent requests.
# It has only one method: ping(int t), where t represents some time in milliseconds.
# Return the number of pings that have been made from 3000 milliseconds ago until now.
# Any ping with time in [t - 3000, t] will count, including the current ping.
# It is guaranteed that every call to ping uses a strictly larger value of t than before.

import collections
class RecentCounter:

    def __init__(self):
        self.p = collections.deque()

    def ping(self, t):
        self.p.append(t)
        while self.p[0] < t - 3000:
            self.p.popleft()
        return len(self.p)

if __name__=="__main__":
    obj = RecentCounter()
    param_1 = obj.ping(642)
    param_2 = obj.ping(1849)
    param_3 = obj.ping(4921)
    param_4 = obj.ping(5936)
    param_5 = obj.ping(5957)
    print(param_1, param_2, param_3, param_4, param_5)