class Solution:
    def searchInsert(self, nums, target):
       
        if target <= nums[0]:
            return 0
        
        if target > nums[-1]:
            return len(nums)
        
        for i in range(len(nums) - 1):
            if nums[i+1] == target:
                return i+1
            
            if nums[i+1] > target and nums[i] < target:
                return i+1     

        # return bisect.bisect_left(nums,target)
        # return len([i for i in nums if i < target])
