class Solution:
    def uncommonFromSentences(self, A, B):
        
        a = A.split()
        b = B.split()
        c = a + b
         
        old = set()
        new = set()
        
        for w in c:
            if w not in new:
                new.add(w)
            else:
                old.add(w)
        return list(new.difference(old))
