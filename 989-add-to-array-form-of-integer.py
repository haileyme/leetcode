class Solution(object):
    def addToArrayForm(self, A, K):
        A = ''.join([str(x) for x in A])
        result = int(A) + K
        result = list(str(result))
        result = [int(x) for x in result]
        return result
