s = False
while s == False:
    print("SUBSTRINGS CATCHER")
    fr = input("Write a phrase:").lower()
    pala = input("Write a word:").lower()
    quan = 0
    for i in range(len(fr) - len(pala)):
        if fr[i:i + len(pala)] == pala: quan += 1
    print("The word", pala, "appear", quan , "times in the phrase.")
    p = False
    while p == False:
        m = input("Wanna quit the program? (y/n)")
        if m == "y" or m == "Y":
            p = True
            s = True
        elif m != "n" or m != "N":
            print("Digito inválido")
        else:
            p = True
