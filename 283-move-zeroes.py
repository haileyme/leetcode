class Solution:
    def moveZeroes(self, nums):
        counter = 0
        
        while (0 in nums):
            nums.remove(0)
            counter += 1
            
        while (counter != 0):
            nums.append(0)
            counter -= 1
            
        '''
        for i in nums:
            if i == 0:
                nums.append(0)
                nums.remove(i)
        '''
