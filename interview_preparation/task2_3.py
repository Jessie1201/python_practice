'''
The company has offices in several locations. Currently someone is at locationA and he needs to get to locationB.
Find the fastest route to get there and return the number of steps.

Input

Inputs:
from_array - an array of integers.
to_array - an array of integers .
The i-th pair (from_array[i], to_array[i]) means that there is a path from location from_array[i] to location to_array[i].

Constraints:
from_array and to_array will have between 0 and 50 integers, inclusive.
each integer in from_array and to_array will be between 0 and 50, inclusive.
Expected execution time is below 10 seconds.

Output:
An integer giving the number to steps to get from location A to location B. If it is not possible return -1.

Examples:
fastestRoute([0, 0, 1], [1, 2, 3], 2, 3) returns 3 since to get from location 2 to location 3 the path is 2 -> 0 -> 1 -> 3, which is 3 steps.
fastestRoute([0, 1], [2, 3], 0, 1) returns -1 since it is there is no path from location 0 to location 1.
'''

# the solution below has not pass 1/4 test cases
class Solution:
    def fastestroute(self, from_array,to_array,locationa,locationb):
        # graph stores the possible path starting from each location
        length = len(from_array)
        graph = {}
        for i in range(length):
            if from_array[i] not in graph:
                graph[from_array[i]] = [to_array[i]]
            else:
                if to_array[i] not in graph[from_array[i]]:
                    graph[from_array[i]].append(to_array[i])
            if to_array[i] not in graph:
                graph[to_array[i]] = [from_array[i]]
            else:
                if from_array[i] not in graph[to_array[i]]:
                    graph[to_array[i]].append(from_array[i])
                    
        # recursion with depth-first search
        def getStep(start, end, visited):
            if end in graph[start]:
                return 1
            visited.append(start)
            new_start = []
            for el in graph[start]:
                if el not in visited:
                    new_start.append(el)
            if not new_start:
                return 9999
            return 1 + min([getStep(el, end, visited) for el in new_start])

        res = getStep(locationa, locationb, [])
        if res >= 9999:
            return -1
        else:
            return res


if __name__=="__main__":
    obj = Solution()
    # 5 is the correct answer
    param_1 = obj.fastestroute([9, 13, 19, 15, 23, 7, 16, 17, 9, 8, 21, 16, 21, 23, 18, 7, 4, 14, 23, 14, 8, 21, 23, 8, 19, 0, 7, 5, 14, 20, 14, 8, 19, 23, 3, 19, 2, 1, 20, 6],
                                 [5, 2, 0, 14, 15, 10, 5, 22, 13, 11, 18, 3, 22, 0, 1, 2, 23, 16, 5, 10, 15, 19, 1, 19, 21, 20, 10, 3, 3, 19, 2, 15, 17, 11, 21, 16, 16, 18, 9, 16],1,7)
    # 8 is the correct answer
    # param_1 = obj.fastestroute([2, 18, 18, 23, 29, 21, 23, 17, 23, 11, 11, 18, 27, 14, 4, 14, 5, 16, 6, 13, 28, 11, 8, 23, 0, 17, 27, 20, 2, 1, 26, 20, 23, 23, 21, 18, 13, 24],[17, 23, 26, 15, 19, 28, 17, 3, 25, 5, 18, 17, 6, 18, 22, 0, 1, 17, 21, 3, 16, 24, 5, 11, 16, 21, 19, 25, 27, 28, 5, 25, 24, 28, 4, 20, 27, 25],8,29)
    # param_1 = obj.fastestroute([2, 10, 4, 2, 11, 8, 12, 8, 11, 0, 14, 10, 12, 14],[6, 6, 13, 9, 15, 5, 15, 7, 7, 7, 1, 1, 6, 0],5,9)
    
    print(param_1)