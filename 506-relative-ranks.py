class Solution(object):
    def findRelativeRanks(self, nums):
        result = []
        sorted_nums = sorted(nums)[::-1]
        
        for n in nums:
            rank = sorted_nums.index(n)
            if rank == 0:
                result.append('Gold Medal')
            elif rank == 1:
                result.append('Silver Medal')
            elif rank == 2:
                result.append('Bronze Medal')
            else:
                result.append(str(rank + 1))
        return result
