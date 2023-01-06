s = False
while s == False:
    #Inserir o dia
    dd = int(input("Insira o dia: "))
    #Condicional do dia
    if dd < 1 or dd > 31:
        print("Dia inválido. Tente novamente")
    else:
        #Inserir o mês
        mm = int(input("Insira o mês: "))
        #Condicional do mês
        if mm < 1 or mm > 12:
            print("Mês inválido. Tente novamente")
        #Condicional para mêses que terminam com 30
        elif mm == 4 and dd == 31 or mm == 6 and dd == 31 or mm == 9 and dd == 31 or mm == 11 and dd == 31:
            print("Dia inválido. Tente novamente")
        #Condicional para fevereiro sem contar os anos bissextos
        elif mm == 2 and dd > 29:
            print("Dia inválido. Tente novamente")
        else:
            #Inserir o ano
            aaaa = int(input("Insira o ano: "))
            #Condicional para ano
            if aaaa < 1 or aaaa > 9999:
                print("Ano inválido. Tente novamente")
            #Condicional para dias maiores de 28 em anos não bissextos
            elif aaaa % 4 != 0 and mm == 2 and dd > 28:
                print("Dia inválido. Tente novamente")
            else:
                #Inserir se é antes ou depois de Cristo
                tipo = str(input("a.c ou d.c: "))
                if tipo == "d.c" or tipo == "D.C" or tipo == "d.C" or tipo == "dc" or tipo == "DC" or tipo == "dC":
                #Condicionais para depois de Cristo
                    #Condicional para final do ano e do mês
                    if dd == 31:
                        if mm == 12:
                            print(1,"-",1,"-",aaaa + 1,"d.C")
                        #Condicional para final do mês
                        else:
                            print(1,"-",mm + 1,"-",aaaa,"d.C")
                    #Condicional para meses que terminam com 30
                    elif mm == 4 and dd == 30 or mm == 6 and dd == 30 or mm == 9 and dd == 30 or mm == 11 and dd == 30:
                        print(1,"-",mm + 1,"-",aaaa,"d.C")
                    elif dd == 29 and mm == 2 and aaaa % 4 == 0:
                        print(1,"-",3,"-",aaaa,"d.C")
                    elif dd == 28 and mm == 2 and aaaa % 4 != 0:
                        print(1,"-",3,"-",aaaa,"d.C")
                    elif dd == 28 and mm == 2 and aaaa % 4 == 0:
                        print(dd + 1,"-",mm,"-",aaaa,"d.C")
                    else:
                        print(dd+1, "-",mm, "-", aaaa,"d.C")
                elif tipo == "a.c" or tipo == "A.C" or tipo == "a.C" or tipo == "ac" or tipo == "AC" or tipo == "aC":
                    if aaaa == 1:
                        if dd == 31:
                            if mm == 12:
                                print(1,"-",1,"-",1,"d.C")
                    else:
                        if dd == 31:
                            if mm == 12:
                                print(1,"-",1,"-",aaaa - 1,"a.C")
                            #Condicional para final do mês
                            else:
                                print(1,"-",mm + 1,"-",aaaa,"a.C")
                        #Condicional para meses que terminam com 30
                        elif mm == 4 and dd == 30 or mm == 6 and dd == 30 or mm == 9 and dd == 30 or mm == 11 and dd == 30:
                            print(1,"-",mm + 1,"-",aaaa,"a.C")
                        elif dd == 29 and mm == 2 and aaaa % 4 == 0:
                            print(1,"-",3,"-",aaaa,"a.C")
                        elif dd == 28 and mm == 2 and aaaa % 4 != 0:
                            print(1,"-",3,"-",aaaa,"a.C")
                        elif dd == 28 and mm == 2 and aaaa % 4 == 0:
                            print(dd + 1,"-",mm,"-",aaaa,"a.C")
                        else:
                            print(dd+1, "-",mm, "-", aaaa,"a.C")
    p = False
    while p == False:
        m = input("Deseja sair do programa? (s/n)")
        if m == "s":
            p = True
            s = True
        elif m != "n":
            print("Digito inválido")
        else:
            p = True