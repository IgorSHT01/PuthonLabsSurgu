x = 4**511 + 2**511 - 511
k = 0
while x:
    if x % 2 == 1:
        k += 1
    x//=2
print(k)
