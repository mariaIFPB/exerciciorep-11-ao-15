"""
Faça um programa que peça 10 números inteiros,
calcule e mostre a quantidade de números pares
e a quantidade de números impares.
"""
npar = 0
nimpar = 0
for x in range(10):
    y = int(input("digite um numero:"))
    if y%2 == 0:
        npar += 1
    else:
        nimpar += 1
print("numero pares =",npar,"numeros impares = ",nimpar)
