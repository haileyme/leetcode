class Solution:
    def buddyStrings(self, A: 'str', B: 'str') -> 'bool':
        if len(A) != len(B):
            return False
        else:
            if A == B:
                if len(set(A)) < len(A):
                    return True
                else:
                    return False
            else:
                res = []
                for i in range(len(A)):
                    if A[i] != B[i]:
                        res.append([A[i], B[i]])
                if len(res) != 2:
                    return False
                else:
                    return res[0][0] == res[1][1] and res[0][1] == res[1][0]
