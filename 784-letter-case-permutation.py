class Solution:
    def letterCasePermutation(self, S):
        Slist = [S]
        for i in range(len(S)):
            if S[i].isalpha():
                for item in Slist:
                    individual = list(item)  # individual = ["a","1","b","2"]
                    if individual[i].islower():
                        individual[i] = individual[i].upper()
                    else:
                        individual[i] = individual[i].lower()
                    
                    t = "".join(individual)
                    if t not in Slist:
                        Slist.append(t)
        return Slist
