class Solution:
    def merge(self, nums1, m, nums2, n):
        nums1[:] = nums1[:m]
        nums2[:] = nums2[:n]
        nums1[:] = nums1[:] + nums2[:]
        nums1.sort()
