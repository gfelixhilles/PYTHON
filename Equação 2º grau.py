a = float(input("Insira a: "))
b = float(input("Insira b: "))
c = float(input("Insira c: "))

delta = (b**2) - (4*a*c)

print(delta)
if a == 0:
    print("Erro!  Divisão  por  zero!")
else:
    if delta < 0:
        print("Não Existe raiz real")
    elif delta == 0:
        print("existe uma raiz real, e ela é:",end=" ")
        print( (b*-1) / (2*a) )
    else:
        print("existem duas raízes reais, e elas são:")
        print("x1 = ", ((b*-1)+(delta**0.5)) / (2*a))
        print("x2 = ", ((b*-1)-(delta**0.5)) / (2*a))