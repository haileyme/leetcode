class Solution:
    def customSortString(self, S, T):
        return ''.join(sorted(list(T), key = lambda x: S.find(x)))
