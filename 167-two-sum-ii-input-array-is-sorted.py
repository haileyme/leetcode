class Solution:
    def twoSum(self, numbers, target):

        start = 0
        end = len(numbers)-1
        result = []
        
        while start < end:
            if(numbers[start] + numbers[end] < target):
                start += 1
            elif(numbers[start] + numbers[end] > target):
                end -= 1
            elif(numbers[start] + numbers[end] == target):
                result.append(start+1)
                result.append(end+1)
                break
                
        return result
