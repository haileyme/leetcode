class Solution:
    def dailyTemperatures(self, T):
        if len(T) == 0:
            return 0

        daywait = [0] * (len(T))

        for i in range(len(T) - 2, -1, -1):
            start = i
            end = i + 1
            days = 0

            while(True):

                if T[start] < T[end]:
                    days = end - start
                    break

                else:
                    if daywait[end] == 0:
                        break
                    else:
                        end += daywait[end]

            daywait[i] = days

        return daywait
