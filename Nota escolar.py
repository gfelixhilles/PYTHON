nota1 = int(input("Digite a primeira nota:"))
nota2 = int(input("Digite a segunda nota:"))
soma = nota1 + nota2
if soma >= 60:
    print("Aprovado")
elif soma < 60:
    print("Reprovado")