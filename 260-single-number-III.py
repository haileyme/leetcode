class Solution:
    def singleNumber(self, nums):
        have = set()

        for i in nums:
            if i not in have:
                have.add(i)
            else:
                have.remove(i)
        return list(have)
