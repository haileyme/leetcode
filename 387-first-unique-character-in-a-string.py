class Solution:
    def firstUniqChar(self, s):
        newList = []
        for i in s:
            if i not in newList:
                newList.append(i)
        for j in newList:
            if s.count(j) == 1:
                return s.index(j)
        return -1
