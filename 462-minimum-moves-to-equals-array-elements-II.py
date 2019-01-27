class Solution:
    def minMoves2(self, nums):
        nums = sorted(nums)
        median = nums[len(nums) // 2]
        result = 0
        for n in nums:
            result += abs(n-median)
        return result
