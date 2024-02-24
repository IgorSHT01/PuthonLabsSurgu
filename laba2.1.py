from itertools import product
k=0
abc=product('abcde',repeat=5)
for a in abc:
    x=''.join(a)
    if x[0]!='e' and x[4]!='a':
        k +=1
print(k)