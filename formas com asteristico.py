escolha = input("Meio Diamante, Diamante:")
n = int(input('Entre com um número: '))
if escolha == "meio diamante" or escolha == "meio":
    j = ""
    if n == 1:
        print("*")
    if n == 0:
        print("")
    if n != 1 and n != 0:
        while len(j)<n:      
            j += "*"
            print(j)
        while len(j)>1:
            j = j.replace("*", "",1)
            print(j)
elif escolha == "diamante" or escolha == "Diamante":
    j = "  "
    c = 0
    if n == 1:
        print("**")
    if n == 0:
        print("")
    if n != 1 and n != 0:
        j = (j * (n - 1)) + "**"
        j = j.replace(" ", "",n - 2)
        print(j)
        while c < n - 1:
            j = j + "**"
            j = j.replace("  ", " ", 1)
            print(j)
            c += 1
        while c > 0:
            j = j.replace("**", " ", 1)
            print(j)
            c -= 1