class Solution:
    def dominantIndex(self, nums):
        maxValue = max(nums)
        index = nums.index(maxValue)

        for i in range(len(nums)):
            if maxValue < nums[i] * 2 and i != index:
                return -1
        return index
