class Solution:
    def romanToInt(self, s):
        roman = ['I', 'IV', 'V', 'IX', 'X', 'XL', 'L', 'XC', 'C', 'CD', 'D', 'CM', 'M']
        number = [1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900, 1000]

        result = 0
        while s:
            if len(s)==1:
                result += number[roman.index(s)]
                break
            elif s[:2] in roman:
                result += number[roman.index(s[:2])]
                s = s[2:]
            else:
                result += number[roman.index(s[:1])]
                s = s[1:]
        return result
