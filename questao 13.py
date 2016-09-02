base = int(input("digite um valor: "))
expoente = int(input("digite um valor: "))
cont = 0
produto = 1
while cont < expoente:
    produto = produto*base
    cont = cont + 1

print(base, "elevado a " ,expoente ,"é igual a", produto)
