class Solution:
    def findWords(self, words):
        rows = [list('qwertyuiop'), list('asdfghjkl'), list('zxcvbnm')]
        
        result = [w for w in words for row in rows if set(w.lower()).issubset(row)]
        
        return result
