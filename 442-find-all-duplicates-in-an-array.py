class Solution:
    def findDuplicates(self, nums):
        result = []
        onlyone = set()
        for num in nums:
            if num not in onlyone:
                onlyone.add(num)
            else:
                result.append(num)
        return result
