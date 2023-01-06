#-*- coding: utf-8 -*-
"""
Calculadora v2
Autor: Gabriel Felix
Função: fazer contas como soma, divisão, multiplicação e subtração
"""

print("___________CALCULADORA V2.0_____________")
sair = False
while sair == False:
	num1 = input("Digite o primeiro número:")
	num1 = int(num1)
	operador = input("Digite o operador(+-/*):")
	num2 = input ("Digite o segundo numero:")
	num2 = int(num2)
	# + soma
	if operador == "+":
		operação = num1 + num2
	# - subtrção
	if operador == "-":
		operação = num1 - num2
	# / divisão
	if operador == "/":
		operação = num1 / num2
	# * multiplicação
	if operador == "*":
		operação = num1 * num2
############################################
	print("Resultado:")
	print(operação)
	teste = input("Deseja sair da calculadora?(s/n):")
	if teste == "s" or teste == "S":
		sair = True