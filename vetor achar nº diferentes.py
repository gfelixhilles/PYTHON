# -*- coding: utf-8 -*-
vet = []
dif = 0
for i in range(10):
    vet.append(input(f"Digite o {i+1}º número:"))
for i in range(10):
    if vet.count(vet[i]) == 1:
        dif += 1
print(dif)