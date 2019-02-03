class Solution(object):
    def findPairs(self, nums, k):
        count=0
        c=collections.Counter(nums)
        for i in c:
            if (k>0 and i+k in c) or (k==0 and c[i]>1):
                count+=1
        return count
