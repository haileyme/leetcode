a=["j je", "b fjt", "7 zbr", "m le", "o 33"]
b=[]
c=[]
for i in range(len(a)):
    if(a[i].split()[1].isalpha()==True):
        b.append(a[i])
        c=sorted(b, key=lambda x: (x[x.find(" "):])) # find():

for i in range(len(a)):
    if(a[i].split()[1].isdigit()==True):
        c.append(a[i])
print(c)
