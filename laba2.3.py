n=10
def m(n):
    k = 0
    m = 1
    for i in range(2,n+1):
        if n%i == 0:
            k += 1
            m = m * i
            if k==5:
                break
    if k < 5:
        x = 0
    else:
        x = m
    
    return x

a=m(n)
print(a)

k = 0 
for i in range(200000001,200010000):
    f = m(i)
    if 0 < f < i:
        print(f)
        k += 1
        if k == 5:
            break

