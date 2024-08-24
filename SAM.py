# Making function to turn decimal into binary
def binary(n):
    # b is the array of each 0 and 1
    b = []
    if n == 0:
        return 0
    while n != 0:
        b.append(n%2)
        n = n // 2
    # Inverting the order of b
    b.reverse()
    return b

# Making function to do square-and-multiply
def sam(b, p, m):
    # r is the counter (result of the operations. Ex: r = 1; b¹ * b¹ = b² -> r = 2; b² * b² = b^4 ...)
    r = 1
    if p == 0:
        return p+1
    else:
        # Turning p into binary and removing the first 1
        p = binary(p)
        p.pop(0)
        for i in p:
            if i == 0:
                r = r+r
                print("____________________________________________________")
                print(f"{b}^{r} mod({m}) ≡ {(b**r)%m}")
            else:
                r = r+r+1
                print("____________________________________________________")
                print(f"{b}^{r-1} mod({m}) ≡ {(b**(r-1)) % m}")
                print(f"{b}*({b}^{r-1}) mod({m}) ≡ {(b*(b**(r-1))) % m}")
# Making the input and printing the result
print(sam(int(input("Digit the base: ")), int(input("Digit the power: ")), int(input("Digit the modulus: "))))
