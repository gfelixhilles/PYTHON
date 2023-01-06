print("ROMAN NUMBERS CONVERTER")
num = int(input("Digit the number:"))
if num < 0:
    print("Tente novamente")
else:
    u = num // 1 % 10
    if u == 0:
        u = ""
    elif u == 1:
        u = "I"
    elif u == 2:
        u = "II"
    elif u == 3:
        u = "III"
    elif u == 4:
        u = "IV"
    elif u == 5:
        u = "V"
    elif u == 6:
        u = "VI"
    elif u == 7:
        u = "VII"
    elif u == 8:
        u = "VIII"
    elif u == 9:
        u = "IX"
    d = num // 10 % 10
    if d == 0:
        d = ""
    elif d == 1:
        d = "X"
    elif d == 2:
        d = "XX"
    elif d == 3:
        d = "XXX"
    elif d == 4:
        d = "XL"
    elif d == 5:
        d = "L"
    elif d == 6:
        d = "LX"
    elif d == 7:
        d = "LXX"
    elif d == 8:
        d = "LXXX"
    elif d == 9:
        d = "XC"
    c = num // 100 % 10
    if c == 0:
        c = ""
    elif c == 1:
        c = "C"
    elif c == 2:
        c = "CC"
    elif c == 3:
        c = "CCC"
    elif c == 4:
        c = "CD"
    elif c == 5:
        c = "D"
    elif c == 6:
        c = "DC"
    elif c == 7:
        c = "DCC"
    elif c == 8:
        c = "DCCC"
    elif c == 9:
        c = "CM"
    m = num // 1000 % 10
    if m == 0:
        m = ""
    elif m == 1:
            m = "M"
    elif m == 2:
        m = "MM"
    elif m == 3:
        m = "MMM"
    print(m+c+d+u)