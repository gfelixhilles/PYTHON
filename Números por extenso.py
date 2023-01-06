print('Conversor de números por extenso')


num = input('Digite o número:')
num = str(num)
if len(num) == 6:
    pass
elif len(num) == 5:
    num = "0" + num
elif len(num) == 4:
    num = "00" + num
elif len(num) == 3:
    num = "000" + num
elif len(num) == 2:
    num = "0000" + num
elif len(num) == 1:
    num = "00000" + num
u = ""
d = ""
c = ""
esp = ""
if num == "1000000":
    print("um milhâo")
elif len(num) > 6 or len(num) == 0:
    print("Erro. Tente novamente")
else:
    def unidades(u):
        u = int(u)
        if u == 0:
            return ""
        if u == 1:
            return "um"
        if u == 2:
            return "dois"
        if u == 3:
            return "três"
        if u == 4:
            return "quatro"
        if u == 5:
            return "cinco"
        if u == 6:
            return "seis"
        if u == 7:
            return "sete"
        if u == 8:
            return "oito"
        if u == 9:
            return "nove"

    def especial(esp):
        esp = int(esp)
        if esp == 0:
            return "dez"
        if esp == 1:
            return "onze"
        if esp == 2:
            return "doze"
        if esp == 3:
            return "treze"
        if esp == 4:
            return "quatorze"
        if esp == 5:
            return "quinze"
        if esp == 6:
            return "dezesseis"
        if esp == 7:
            return "dezessete"
        if esp == 8:
            return "dezoito"
        if esp == 9:
            return "dezenove"
    def dezenas(d):
        d = int(d)
        if d == 0:
            return ""
        if d == 1:
            return especial(d)
        if d == 2:
            return "vinte"
        if d == 3:
            return "trinta"
        if d == 4:
            return "quarenta"
        if d == 5:
            return "cinquenta"
        if d == 6:
            return "sessenta"
        if d == 7:
            return "setenta"
        if d == 8:
            return "oitenta"
        if d == 9:
            return "noventa"
    def centena(c):
        c = int(c)
        if c == 0:
            return ""
        if c == 1:
            return "cento"
        if c == 2:
            return "duzentos"
        if c == 3:
            return "trezentos"
        if c == 4:
            return "quatrocentos"
        if c == 5:
            return "quinhentos"
        if c == 6:
            return "seiscentos"
        if c == 7:
            return "setecentos"
        if c == 8:
            return "oitocentos"
        if c == 9:
            return "novecentos"
    parte_1 = ""
    parte_2 = ""
    c = centena(num[0])
    d = dezenas(num[1])
    u = unidades(num[2])
    esp = especial(num[2])
    c2 = centena(num[3])
    d2 = dezenas(num[4])
    u2 = unidades(num[5])
    esp2 = especial(num[5])
    #if c é a mesma coisa que if se não é nulo. Assim como if not c é a mesma coisa que if c é nulo;
    if c and d and u:
        if num[1] == "1":
            parte_1 = c + " e " + esp + " mil"
        else:
            parte_1 = c + " e " + d + " e " + u + " mil"
    elif c and d and not u:
        if num[1] == "1":
            parte_1 = c + " e " + esp + " mil"
        else:
            parte_1 = c + " e " + d + " mil"
    elif c and not d and u:
        parte_1 = c + " e " + u + " mil"
    elif c and not d and not u:
        if num[0] == "1":
            parte_1 = "cem mil"
        else:
            parte_1 = c + " mil"
    elif not c and d and u:
        if num[1] == "1":
            parte_1 = esp + " mil"
        else:
            parte_1 = d + " e " + u + " mil"
    elif not c and d and not u:
        if num[1] == "1":
            parte_1 = esp + " mil"
        else:
            parte_1 = d + " mil"
    elif not c and not d and u:
        parte_1 = u + " mil"
    elif not c and not d and not u:
        parte_1 = ""








    if c2 and d2 and u2:
        if num[4] == "1":
            parte_2 = c2 + " e " + esp2
        else:
            parte_2 = c2 + " e " + d2 + " e " + u2
    elif c2 and d2 and not u2:
        if num[4] == "1":
            parte_2 = c2 + " e " + esp2
        else:
            parte_2 = c2 + " e " + d2
    elif c2 and not d2 and u2:
        parte_2 = c2 + " e " + u2
    elif c2 and not d2 and not u2:
        if num[3] == "1":
            parte_2 = "cem"
        else:
            parte_2 = c2
    elif not c2 and d2 and u2:
        if num[4] == "1":
            parte_2 = esp2
        else:
            parte_2 = d2 + " e " + u2
    elif not c2 and d2 and not u2:
        if num[4] == "1":
            parte_2 = esp2
        else:
            parte_2 = d2
    elif not c2 and not d2 and u2:
        parte_2 = u2
    elif not c2 and not d2 and not u2:
        parte_2 = ""
    if parte_1:
        if not parte_2:
            print(parte_1)
        if c2 and not d2 and not u2 or not c2 and d2 and not u2 or not c2 and not d2 and u2 or not c2 and num[4] =="1":
            print(parte_1, "e", parte_2)
        else:
            print(parte_1 + ",", parte_2)
    else:
        print(parte_2)