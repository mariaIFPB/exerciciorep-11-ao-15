"""
A série de Fibonacci é formada pela seqüência
1,1,2,3,5,8,13,21,34,55,...
Faça um programa capaz de gerar a série até o n−ésimo termo.
"""
n = eval(input("qual o n-esimo termo?"))
x = 0
y = 0
z = 0
if (n >= 2):
    for m in range(n):
        print(z)
        if (z == 0):
            y = 1
        x = y
        y = z
        z = x+y
else:
    print("numero invalido")
