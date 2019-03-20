# Given a sorted array nums, remove the duplicates in-place such that each element appear only once and return the new length.
# Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

def removeDuplicates(nums):
    while len(list(set(nums))) != len(nums):
        for el in nums:
            if el in nums[:nums.index(el)] or el in nums[nums.index(el)+1:]:
                nums.remove(el)
    return nums

if __name__=="__main__":
    print(removeDuplicates([-1,0,0,0,0,3,3]))