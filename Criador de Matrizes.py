import random as rd
# Quantas linhas e colunas a matriz terá
ql = int(input("Digite quantas linhas:"))
qc = int(input("Digite quantas colunas:"))
# Criação da Matriz
m = []
in1 = input("Inserção manual de dados ou automática(m/a):")
if in1 == "a":
    # Há um vetor para cada linha
    for i in range(ql):
        m.append([])
        # Lê um valor e insere no seu respectivo vetor
        for j in range(qc):
            m[i].append(rd.randrange(1, 100))
    # Tira os colchetes da linhas e colunas e os coloca em ordem
    for i in range(ql):
        for j in range(qc):
            print(f"{m[i][j]:02}", end = " ")
        print()
elif in1 == "m":
    # Há um vetor para cada linha
    for i in range(ql):
        m.append([])
        # Lê um valor e insere no seu respectivo vetor
        for j in range(qc):
            m[i].append(int(input(f"Digite o valor da {i+1}ª linha da {j+1}ª coluna:")))
# Tira os colchetes da linhas e colunas e os coloca em ordem
    for i in range(ql):
        for j in range(qc):
            print(f"{m[i][j]:02}", end = " ")
        print()
else:
    print("Opcao invalida fila duma puta!!!")
