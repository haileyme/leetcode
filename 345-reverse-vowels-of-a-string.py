    def reverseVowels(self, s):
        string = []
        vowel = []
        
        for x in s:
            string.append(x)
        
        for x in s:
            if x in ['a','A','e','E','i','I','o','O','u','U']:
                vowel.append(x)
        vowel.reverse()
        i = 0
        
        for x in range(0,len(string)):
            if string[x] in ['a','A','e','E','i','I','o','O','u','U']:
                string[x] = vowel[i]
                i += 1
                
        return ''.join(string)
