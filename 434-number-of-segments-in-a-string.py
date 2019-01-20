class Solution:
    def countSegments(self, s):
        s = s.strip()
        if len(s) == 0:
            return 0

        count = 0
        new = s.split(' ')

        for i in new:
            if len(i.strip()) != 0:
                count += 1
        return count
