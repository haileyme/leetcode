class Solution(object):
    def shortestCompletingWord(self, licensePlate, words):
        plate = [s.lower() for s in licensePlate if s.isalpha()]
        for word in sorted(words, key=len):
            temp = copy.copy(plate)
            for w in word:
                if w in temp:
                    del temp[temp.index(w)]
            if len(temp) == 0:
                return word
