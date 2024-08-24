def binario(n):
    b = []
    if n == 0:
        return n+n
    while n != 0:
        b.append(n%2)
        n = n // 2
    b.reverse()
    return b
def sam(b, e, N):
    r = 1
    if e == 0:
        return e+1
    else:
        e = binario(e)
        e.pop(0)
        print(e)
        for i in e:
            if i == 0:
                r = r+r
                print("____________________________________________________")
                print(f"{b}^{r} mod({N}) ≡ {(b**r)%N}")
            else:
                r = r+r+1
                print("____________________________________________________")
                print(f"{b}^{r-1} mod({N}) ≡ {(b**(r-1)) % N}")
                print(f"{b}*({b}^{r-1}) mod({N}) ≡ {(b*(b**(r-1))) % N}")
print(sam(int(input("Digit the base: ")), int(input("Digit the power: ")), int(input("Digit the modulus: "))))