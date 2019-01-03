class Solution(object):
    def findDisappearedNumbers(self, nums):
        distinct_nums = set(nums)
        result = []
        for i in range(1, len(nums)+1):
            if i not in distinct_nums:
                result.append(i)
        
        return result
