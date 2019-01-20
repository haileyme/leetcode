class Solution:
    def partitionLabels(self, S):
        dic = {}
        for i, c in enumerate(S):
            dic[c] = i

        cur_max = 0
        result = []
        count = 0

        for i, c in enumerate(S):
            count += 1
            cur_max = max(cur_max, dic[c])

            if cur_max == i:
                result.append(count)
                count = 0
        return result
