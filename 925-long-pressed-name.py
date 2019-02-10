class Solution:
    def isLongPressedName(self, name: 'str', typed: 'str') -> 'bool':
        i = 0
        for j in range(len(typed)):
            if i < len(name) and name[i] == typed[j]:
                # 0<4 & 0=0, a=a
                # 1<4 & 1=0, l=a
                # 2<4 & 1=2, l=l
                # 2<4 & 2=3, e=e
                # 3<4 & 3=4, x=e
                # 3<4 & 3=5, x=x
                i += 1
            elif j == 0 or typed[j] != typed[j-1]:
                # 1==0 or 1=0, a=a
                # 4==0 or 4=3, e=e
                return False
        return i == len(name)
