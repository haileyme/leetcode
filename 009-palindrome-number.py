class Solution:
    def isPalindrome(self, x):
        if x < 0:
            return False
        elif x == 0:
            return True
        
        srtNum = str(x)
        start = 0
        end = len(srtNum) - 1
        
        while start < end:
            if srtNum[start] == srtNum[end]:
                start += 1
                end -= 1
            else:
                return False
                
        return True
