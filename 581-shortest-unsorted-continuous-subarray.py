class Solution(object):
    def findUnsortedSubarray(self, nums):
        snums = sorted(nums)
        s = e = -1
        for i in range(len(nums)):
            if nums[i] != snums[i]:
                if s == -1: s = i
                e = i
        return e - s + 1 if e != s else 0
