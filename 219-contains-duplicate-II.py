class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        if len(nums) == 0 or k <= 0:
            return False

        dic = {}
        for i, num in enumerate(nums):
            if num in dic and abs(i - dic[nums[i]]) <= k:
                return True
            dic[num] = i
        return False
