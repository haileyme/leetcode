A = 'abcde'
B = 'deabc'

a = list(A)
for i in range(len(A)):
    a.insert(len(a),a[0])
    a.pop(0)
    if(a==list(B)):
        print(True)
        break
    if(i==len(A)-1):
        print(False)
