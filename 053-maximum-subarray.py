class Solution:
    def maxSubArray(self, nums):
        maxsum = nums[0]
        maxhere = nums[0]
        
        for i in range(1, len(nums)):
            if maxsum >= 0:
                maxsum += nums[i]
            else:
                maxsum = nums[i]
            maxhere = max(maxhere, maxsum)
        return maxhere
