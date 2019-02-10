class Solution:
    def singleNumber(self, nums: 'List[int]') -> 'int':
        s1 = sum(nums)
        s2 = sum(set(nums))

        r = 3*s2 - s1
        return r//2
