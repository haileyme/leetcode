class Solution:
    def repeatedSubstringPattern(self, s):
        if not s:
            return False
            
        addList = (s + s)[1:-1]
        return addList.find(s) != -1
