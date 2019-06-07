ni1=input()
c11=1
for i1 in range(len(ni1)-1):
    a1=ni1[i1]+ni1[i1+1]
    b1=int(a1)
    if b1<=26 and ni1[i1]!="0":
        c11+=1
if c11==3:
    print(c11)
else:
    print(c11+(c11-1)//2)
