class Solution:
    def reverseWords(self, s):
        return(" ".join(list(reversed(s[::-1].split(" ")))))
