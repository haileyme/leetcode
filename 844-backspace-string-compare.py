class Solution:
    def backspaceCompare(self, S, T):
        a = ""
        b = ""
        
        for i in S:
            if i == '#':
                a = a[:-1]
            else:
                a += i
        
        for i in T:
            if i == '#':
                b = b[:-1]
            else:
                b += i
                
        return a == b
