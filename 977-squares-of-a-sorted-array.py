class Solution:
    def sortedSquares(self, A):
        calnums = list(map(lambda x: x**2, A))
        calnums.sort()
        return calnums
